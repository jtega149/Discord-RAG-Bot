import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from db.vector_store import query_documents

def retrieve_pdfs(query: str, k: int = 1) -> list[dict]:
    """
    Takes a user's search query, finds the most relevant PDFs
    in ChromaDB, and returns a list of dicts containing the
    filename and file path for each match.
    """
    results = query_documents(query, k=k)

    if not results:
        return []

    # Extract just the filename and file path from each result's metadata
    # This is what gets passed to Discord to send the actual files back
    matches = []
    for result in results:
        matches.append({
            "filename": result.metadata["filename"],
            "file_path": result.metadata["file_path"],
            "summary": result.page_content
        })

    return matches