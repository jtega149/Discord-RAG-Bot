
from langchain_community.document_loaders import PyMuPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
"""
PDF file → extract text → split into chunks → convert to vectors → store in ChromaDB
Claude dummy code we must check later...
"""

def ingest_pdf(file_path: str, course: str):
    # Load the PDF
    loader = PyMuPDFLoader(file_path)
    documents = loader.load()

    # Split into chunks
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50
    )
    chunks = splitter.split_documents(documents)

    # Tag each chunk with the course name
    for chunk in chunks:
        chunk.metadata["course"] = course

    return chunks