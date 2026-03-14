# endee-semantic-search
# Endee Semantic Search

This project demonstrates a simple **semantic search system** built using transformer-based embeddings and vector similarity search.

Unlike traditional keyword search, semantic search understands the **meaning of a query** and retrieves the most relevant documents based on vector similarity.

---

## Project Overview

The pipeline works as follows:

1. Documents are converted into **vector embeddings** using a SentenceTransformer model.
2. These embeddings are stored in a **vector storage layer**.
3. A user query is also converted into an embedding.
4. Cosine similarity is used to retrieve the **most relevant documents**.

---

## Architecture

Documents  
↓  
SentenceTransformer Embeddings (all-MiniLM-L6-v2)  
↓  
Vector Storage Layer (Endee-compatible abstraction)  
↓  
Cosine Similarity Search  
↓  
Top-K Relevant Documents

---

## Project Structure

backend/  
  embeddings.py → Generates embeddings using SentenceTransformer  
  vector_store.py → Vector storage abstraction  

scripts/  
  ingest_docs.py → Document ingestion pipeline  

test_query.py → Runs semantic search queries  
requirements.txt → Python dependencies  

---

## Installation
git clone https://github.com/durg-giri123/endee-semantic-search.git

cd endee-semantic-search


Install dependencies:


pip install -r requirements.txt


---

## Run Document Ingestion

Convert documents into embeddings and store them:


python -m scripts.ingest_docs


---

## Run Semantic Search

Run the query script:


python test_query.py


Example Output:


Query: How does binary search work?

Top results:

0.74 Binary search works on sorted arrays.
0.36 Binary lifting is used to compute LCA in trees.
0.29 Segment trees allow efficient range queries.


---

## Endee Integration

The architecture is designed to integrate with the **Endee Vector Database** for scalable vector storage.

Due to write API restrictions in the OSS container build, this project demonstrates the retrieval pipeline using a local vector store abstraction. The same interface can be connected directly to Endee’s API for production vector indexing.

---

## Technologies Used

- Python
- SentenceTransformers
- Cosine Similarity
- Vector Search
- Endee Vector Database (architecture integration)

---

## Author

Durgesh Giri  
B.Tech CSE Student
Sec - 65
Admission No. - 23SCSE1012420

Clone the repository:
