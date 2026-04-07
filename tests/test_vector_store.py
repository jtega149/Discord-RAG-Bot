import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from rag.ingestor import ingest_pdf
from db.vector_store import store_chunks, query_chunks

def test_vector_store():
    # Ingest the pdf and get the chunks
    chunks = ingest_pdf("./Calculus_2_Study_Guide.pdf", "Calc 2")

    # Store the chunks into ChromaDB
    store_chunks(chunks)

    # Test the querying vector store by asking a question related to the material and printing the results
    results = query_chunks("What is the fundamental theorem of calculus?", "Calc 2")
    
    for i, result in enumerate(results):
        print(f"\n--- Result {i+1} ---")
        print(result.page_content)
        print("Metadata:", result.metadata)
    
test_vector_store()