from backend.embeddings import generate_embedding
from backend.vector_store import insert_vector

documents = [
    "Binary search works on sorted arrays.",
    "Segment trees allow efficient range queries.",
    "Binary lifting is used to compute LCA in trees.",
    "Dynamic programming solves overlapping subproblems."
]

for doc in documents:
    print(f"Processing: {doc}")

    embedding = generate_embedding(doc)

    result = insert_vector(
        embedding,
        {"text": doc}
    )

    print("Inserted:", result)

print("Documents indexed successfully.")