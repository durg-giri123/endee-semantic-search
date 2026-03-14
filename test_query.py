from backend.embeddings import generate_embedding
from backend.vector_store import insert_vector, search

docs = [
    "Binary search works on sorted arrays.",
    "Segment trees allow efficient range queries.",
    "Binary lifting is used to compute LCA in trees.",
    "Dynamic programming solves overlapping subproblems."
]

# ingest documents
for d in docs:
    vec = generate_embedding(d)
    insert_vector(vec, {"text": d})

# query
query = "How does binary search work?"

query_vec = generate_embedding(query)

results = search(query_vec)

print("Top results:")
for score, payload in results:
    print(score, payload["text"])