import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from rag.ingestor import ingest_pdf

def test_ingest_pdf():
    chunks = ingest_pdf("./Calculus_2_Study_Guide.pdf", "Calc 2")
    assert len(chunks) > 0, "No chunks were created from the PDF"
    for i in range(len(chunks)):
        print(f"Chunk {i+1}:")
        print(f"Content: {chunks[i].page_content}")

test_ingest_pdf()

