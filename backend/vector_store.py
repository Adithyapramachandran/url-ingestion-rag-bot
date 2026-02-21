# Integrate FAISS vector storage and similarity search
# vector_store.py

from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

model = SentenceTransformer("all-MiniLM-L6-v2")


class VectorStore:

    def __init__(self):
        self.index = None
        self.texts = []

    # ---------- BUILD ----------
    def build(self, chunks):

        if not chunks:
            print("❌ No chunks to embed")
            return

        emb = model.encode(chunks)

        if len(emb) == 0:
            print("❌ Embeddings empty")
            return

        emb = np.array(emb).astype("float32")

        dim = emb.shape[1]

        self.index = faiss.IndexFlatL2(dim)
        self.index.add(emb)

        self.texts = chunks

        print("FAISS index size:", self.index.ntotal)

    # ---------- SEARCH ----------
    def search(self, query, k=5):

        if self.index is None:
            print("❌ Index not built")
            return []

        q = model.encode([query])
        q = np.array(q).astype("float32")

        D, I = self.index.search(q, k)

        results = []
        for i in I[0]:
            if i < len(self.texts):
                results.append(self.texts[i])

        return results
