import json
from pathlib import Path

import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

INPUT_FILE = Path("data/questions/rag_documents.json")
INDEX_DIR = Path("data/vector_store")

INDEX_DIR.mkdir(parents=True, exist_ok=True)

print("=" * 70)
print("BUILDING FAISS INDEX")
print("=" * 70)

# 1. Load RAG documents
with open(INPUT_FILE, "r", encoding="utf-8") as f:
    documents = json.load(f)

print(f"\nDocuments loaded: {len(documents)}")

# 2. Load embedding model
print("\nLoading embedding model...")

model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

# 3. Extract text
texts = [doc["text"] for doc in documents]

# 4. Generate embeddings
print("Generating embeddings...")

embeddings = model.encode(
    texts,
    show_progress_bar=True,
    convert_to_numpy=True
)

# 5. Normalize embeddings
embeddings = embeddings.astype("float32")
faiss.normalize_L2(embeddings)

print(f"Embedding shape: {embeddings.shape}")

# 6. Create FAISS index
dimension = embeddings.shape[1]

index = faiss.IndexFlatIP(dimension)
index.add(embeddings)

# 7. Save FAISS index
index_file = INDEX_DIR / "questions.index"
faiss.write_index(index, str(index_file))

# 8. Save document mapping
mapping_file = INDEX_DIR / "documents.json"

with open(mapping_file, "w", encoding="utf-8") as f:
    json.dump(documents, f, indent=2, ensure_ascii=False)

print("\n" + "=" * 70)
print("FAISS INDEX CREATED")
print("=" * 70)

print(f"\nVectors indexed : {index.ntotal}")
print(f"Dimension       : {dimension}")
print(f"Index           : {index_file}")
print(f"Mapping         : {mapping_file}")