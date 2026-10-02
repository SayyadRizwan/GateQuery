import json
import faiss
from sentence_transformers import SentenceTransformer

INDEX_FILE = "data/vector_store/questions.index"
DOCUMENTS_FILE = "data/vector_store/documents.json"

# Load FAISS
index = faiss.read_index(INDEX_FILE)

# Load documents
with open(DOCUMENTS_FILE, "r", encoding="utf-8") as f:
    documents = json.load(f)

# Load embedding model
model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

query = input("\nEnter your question/topic: ")

# Convert query to embedding
query_embedding = model.encode(
    [query],
    convert_to_numpy=True
).astype("float32")

# Normalize
faiss.normalize_L2(query_embedding)

# Retrieve top 5
scores, indices = index.search(query_embedding, 5)

print("\n" + "=" * 70)
print("TOP 5 RETRIEVED QUESTIONS")
print("=" * 70)

for rank, (score, idx) in enumerate(zip(scores[0], indices[0]), start=1):
    doc = documents[idx]

    print(f"\n[{rank}] Similarity: {score:.4f}")
    print(f"ID: {doc['id']}")
    print(doc["text"][:700])
    print("-" * 70)
    