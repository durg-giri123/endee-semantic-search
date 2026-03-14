vectors = []

def insert_vector(vector, metadata):
    vectors.append({
        "vector": vector,
        "payload": metadata
    })
    return {"status": "stored", "count": len(vectors)}

def search(query_vector, k=3):
    import numpy as np

    scores = []
    for item in vectors:
        v = np.array(item["vector"])
        q = np.array(query_vector)
        sim = np.dot(v, q) / (np.linalg.norm(v) * np.linalg.norm(q))
        scores.append((sim, item["payload"]))

    scores.sort(reverse=True)
    return scores[:k]