import json
import faiss
from sentence_transformers import SentenceTransformer
from google import genai

# ============================================================
# CONFIGURATION
# ============================================================

INDEX_FILE = "data/vector_store/questions.index"
DOCUMENTS_FILE = "data/vector_store/documents.json"

# Gemini API key
client = genai.Client()

# Embedding model
embedding_model = SentenceTransformer(
    "sentence-transformers/all-MiniLM-L6-v2"
)

# ============================================================
# LOAD FAISS + DOCUMENTS
# ============================================================

index = faiss.read_index(INDEX_FILE)

with open(DOCUMENTS_FILE, "r", encoding="utf-8") as f:
    documents = json.load(f)

print(f"Loaded {len(documents)} documents")
print(f"FAISS vectors: {index.ntotal}")


# ============================================================
# RETRIEVAL
# ============================================================

def retrieve(query, top_k=5):

    query_embedding = embedding_model.encode(
        [query],
        convert_to_numpy=True
    ).astype("float32")

    faiss.normalize_L2(query_embedding)

    scores, indices = index.search(
        query_embedding,
        top_k
    )

    results = []

    for score, idx in zip(scores[0], indices[0]):

        if idx == -1:
            continue

        results.append({
            "score": float(score),
            "document": documents[idx]
        })

    return results


# ============================================================
# GENERATION
# ============================================================

def generate_answer(query, retrieved_documents):

    context = "\n\n".join(
        f"""
--- PYQ {i} ---
{result["document"]["text"]}
Similarity: {result["score"]:.4f}
"""
        for i, result in enumerate(retrieved_documents, start=1)
    )

    prompt = f"""
You are a GATE Computer Science Previous Year Question Paper
Analyzer.

Answer the user's query using the retrieved GATE PYQs below.

IMPORTANT RULES:
1. Use the retrieved PYQs as your primary evidence.
2. Do not invent PYQs, answers, years, or question numbers.
3. If the retrieved context does not contain enough information,
   clearly say that.
4. When discussing a PYQ, mention its year and question number.
5. If an answer key is unavailable, say "Answer key not available"
   instead of guessing.
6. Explain the answer clearly and concisely.
7. If multiple retrieved questions are relevant, compare them.

USER QUERY:
{query}

RETRIEVED PYQs:
{context}
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text


# ============================================================
# MAIN
# ============================================================

def main():

    print("\n" + "=" * 70)
    print("GATE PYQ RAG ANALYZER")
    print("=" * 70)

    query = input("\nAsk your question: ")

    print("\nSearching PYQs...")

    results = retrieve(query, top_k=5)

    print("\nGenerating answer...")

    answer = generate_answer(query, results)

    print("\n" + "=" * 70)
    print("ANSWER")
    print("=" * 70)

    print(answer)


if __name__ == "__main__":
    main()

   