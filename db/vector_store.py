#from langchain_community.vectorstores import Chroma
from langchain_chroma import Chroma # New version of Chroma for langchain
from langchain_openai import OpenAIEmbeddings
from pydantic import SecretStr
import os
from dotenv import load_dotenv
load_dotenv()


# Path to where ChromaDB will save data locally
CHROMA_PATH = "../data/chroma"

# Global vector_store, to avoid creating multiple connections thus more scalable
vector_store = None

def get_vector_store():
    global vector_store
    # Connect to ChromaDB, creates the database if it doesn't exist yet
    if not vector_store:
        embeddings = OpenAIEmbeddings(
            model="text-embedding-3-small",
            api_key=SecretStr(os.getenv("OPENAI_API_KEY") or ""),
            dimensions=384
        )

        # Essentially create Chroma client and connect to the "study_materials" collection, which is where we'll store all our chunks
        vector_store = Chroma(
            collection_name="study_materials",
            embedding_function=embeddings,
            persist_directory=CHROMA_PATH
        )

    return vector_store

