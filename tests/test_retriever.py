import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from rag.retriever import retrieve_pdfs

results = retrieve_pdfs("Pass some of the physics material bro")

for i, match in enumerate(results):
    print(f"\n--- Match {i+1} ---")
    print("Filename:", match["filename"])
    print("File path:", match["file_path"])
    print("Summary:", match["summary"])