import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from rag.ingestor import ingest_pdf

def test_ingest_pdf():
    doc = ingest_pdf('./Calculus_2_Study_Guide.pdf')
    if doc:
        print(f"Summary: {doc.page_content}")
        print(f"Metadata: {doc.metadata}")


test_ingest_pdf()

