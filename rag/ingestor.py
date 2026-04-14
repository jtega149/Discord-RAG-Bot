from langchain_core.documents import Document
from openai import OpenAI
from pydantic import SecretStr
import fitz  # PyMuPDF
import base64
import os
import shutil
from dotenv import load_dotenv
load_dotenv()

STORAGE_PATH = "../storage/pdfs"
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def save_pdf(file_path: str) -> str:
    os.makedirs(STORAGE_PATH, exist_ok=True)
    filename = os.path.basename(file_path)
    destination = os.path.join(STORAGE_PATH, filename)
    shutil.copy2(file_path, destination)
    return destination


def generate_pdf_summary(file_path: str) -> str | None:
    """
    Sends each page of the PDF to OpenAI as an image and generates
    a single summary describing what the document is about.
    This summary is what gets embedded into ChromaDB.
    """
    pdf = fitz.open(file_path)
    page_images = []

    for page_num in range(len(pdf)):
        page = pdf[page_num]

        # Render page as image
        pix = page.get_pixmap(dpi=100)
        image_bytes = pix.tobytes("png")
        image_b64 = base64.standard_b64encode(image_bytes).decode("utf-8")

        page_images.append({
            "type": "image_url",
            "image_url": {
                "url": f"data:image/png;base64,{image_b64}"
            }
        })

    # Add the prompt after all page images
    page_images.append({
        "type": "text",
        "text": (
            "You are summarizing a university study document. "
            "Based on all the pages provided, write a concise summary (3-5 sentences) describing: "
            "what type of document this is (lecture notes, past exam, assignment, study guide, etc.), "
            "what course or subject it belongs to, "
            "and what specific topics it covers. "
            "Be specific so this summary can be used to match student search queries."
        )
    })

    pdf.close()

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        max_tokens=512,
        messages=[{"role": "user", "content": page_images}]
    )

    return response.choices[0].message.content


def ingest_pdf(file_path: str) -> Document | None:
    """
    Main function — saves the PDF and generates a summary.
    Returns a single Document object to be stored in ChromaDB.
    """
    try:
        # Save the PDF to storage
        saved_path = save_pdf(file_path)
        print(f"PDF saved to {saved_path}")

        # Generate a summary of the PDF using Claude vision
        print("Generating summary...")
        summary = generate_pdf_summary(file_path)
        if summary:
            print("Finished creating summary.")

        if not summary:
            raise RuntimeError("Couldn't generate summary")

        # Return a single Document with the summary as content
        # and the file path in metadata so we can retrieve it later
        return Document(
            page_content=summary,
            metadata={
                "file_path": saved_path,
                "filename": os.path.basename(file_path),
            }
        )

    except Exception as e:
        print(f"Error ingesting PDF: {e}")
        return None