from langchain_community.document_loaders import PyMuPDFLoader # For loading PDF documents
from langchain_experimental.text_splitter import SemanticChunker
from langchain_openai import OpenAIEmbeddings
import os
from pydantic import SecretStr

def ingest_pdf(file_path: str, course: str):
    # Load the PDF
    try:
        loader = PyMuPDFLoader(file_path) # Points to pdf file to load
        documents = loader.load() # Returns a document object with content and stuff per page
        """
        Semantic chunking splits based on meaning, not character count.
        This is better for study material because concepts don't always
        end neatly at 500 characters — a full explanation of a topic
        stays together in one chunk instead of getting cut in half.
        """
        # Create embeddings for semantic chunking, aka create create vector representations of the text
        embeddings = OpenAIEmbeddings(
            model="text-embedding-3-small",
            api_key=SecretStr(os.getenv("OPENAI_API_KEY") or ""),
            dimensions=384 # Bump up to 1536 for production later on
        )
        # Split the document into semantically meaningful chunks
        splitter = SemanticChunker(
            embeddings=embeddings, # Need to use embedding model because we need the vectors to determine semantic similarity for chunking
            breakpoint_threshold_type="percentile" # splits whenever semantic similarity drops below a certain percentile
        )

        # Splitting the documents into chunks based on semantic similarity (thing we set up in the splitter above)
        chunks = splitter.split_documents(documents) 

        # Tag each chunk with course name and source file, helps with retrieval later on when we want to know which course a chunk belongs to and where it came from
        for chunk in chunks:
            chunk.metadata["course"] = course

        return chunks
    except Exception as e:
        print(f"Error ingesting PDF: {e}")
        return []