from sentence_transformers import SentenceTransformer
import faiss
import numpy as np
from text import load_documents

model = SentenceTransformer('all-MiniLM-L6-v2')

documents = load_documents()
doc_embeddings = model.encode(documents)

index = faiss.IndexFlatL2(doc_embeddings.shape[1])
index.add(np.array(doc_embeddings))


def retrieve_docs(query, k=3):
    query_embedding = model.encode([query])
    distances, indices = index.search(np.array(query_embedding), k)

    return [documents[i] for i in indices[0]]