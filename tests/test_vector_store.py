import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from db.vector_store import store_document, query_documents
from rag.ingestor import ingest_pdf

"""
Need to adjust for rate limiting later on,
perhaps some prompt engineering to minimize token use
"""

def test_vector_store():

    """
    For testing purposes, first create and store document1, wait a minute
    and then create and store document2, then query as you'd like. Just have
    to do it like this for now cause of the rate limit set on my openai api calls
    Ex use:
        document = ingest_pdf("./MyTest.pdf")
        if not document:
            return
        store_document(document)
    """
    res = query_documents("I have a physics exam coming up and I need to catch up on the material")
    print(res)

test_vector_store()