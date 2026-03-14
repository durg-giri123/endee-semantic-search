from sentence_transformers import SentenceTransformer

# load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

def generate_embedding(text: str):
    vector = model.encode(text)
    return vector.tolist()