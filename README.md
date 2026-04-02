Discord RAG Bot

A Discord bot that answers questions about PDFs using Retrieval-Augmented Generation (RAG). Upload study material PDFs per course and ask questions — the bot fetches relevant content and answers using an LLM.

---

## Project Structure

```
rag-discord-bot/
│
├── bot/
│   ├── __init__.py
│   ├── client.py               # Discord bot setup & event listeners
│   └── commands/
│       ├── __init__.py
│       ├── upload.py           # /upload command — attach a PDF to a course
│       ├── ask.py              # /ask command — ask a question about a course
│       └── list_docs.py        # /list command — see all PDFs for a course
│
├── rag/
│   ├── __init__.py
│   ├── ingestor.py             # PDF parsing & chunking
│   ├── embedder.py             # Turning text chunks into vectors
│   └── retriever.py           # Querying the vector DB + calling the LLM
│
├── db/
│   ├── __init__.py
│   └── vector_store.py        # ChromaDB setup & operations
│
├── data/
│   └── chroma/                 # ChromaDB saves data here (auto-generated)
│
├── .env                        # Your API keys — never commit this
├── .gitignore
├── requirements.txt
├── config.py                   # Global settings (model names, chunk size, etc.)
└── main.py                     # Entry point — runs the bot
```

---

## .env File

Create a `.env` file in the root of the project and add the following:

```
DISCORD_TOKEN=your_discord_bot_token
OPENAI_API_KEY=your_openai_api_key
ANTHROPIC_API_KEY=your_anthropic_api_key
```

### Where to get your keys

- **DISCORD_TOKEN** — Go to https://discord.com/developers, create a new application, go to the **Bot** tab, and copy the token.
- **OPENAI_API_KEY** — Go to https://platform.openai.com/api-keys and create a new secret key.
- **ANTHROPIC_API_KEY** — Go to https://console.anthropic.com/settings/keys and create a new key.

---

## Setup Instructions
```

### 1. Create a virtual environment

A virtual environment keeps your project's dependencies isolated from the rest of your system.

```bash
python -m venv venv
```

### 2. Activate the virtual environment

**Mac/Linux:**
```bash
source venv/bin/activate
```

**Windows:**
```bash
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Add your keys to `.env`

Fill in your API keys as shown in the `.env` section above.

### 5. Run the bot

```bash
python main.py
```

---

## Deactivating the Virtual Environment

When you're done working on the project, you can deactivate the virtual environment with:

```bash
deactivate
```

## Johnny's Discord RAG bot pipeline

### Whenever a User uploads a PDF to the discord
```bash
User runs /upload course:CS101 + attaches a PDF
        ↓
Discord receives the file & course name
        ↓
PyMuPDF extracts all the text from the PDF
        ↓
LangChain splits the text into small chunks (e.g. 500 words each)
        ↓
OpenAI converts each chunk into a vector (a list of numbers that represents meaning)
        ↓
ChromaDB stores each vector + the original text + metadata (course name, filename, page number)
```

### When a User asks a question to the discord bot
```bash
User runs /ask course:CS101 what is dynamic programming?
        ↓
OpenAI converts the question into a vector (same way chunks were converted)
        ↓
ChromaDB searches for the chunks whose vectors are closest to the question vector
        ↓
Only chunks tagged CS101 are searched (metadata filtering)
        ↓
Top 3-5 most relevant chunks are retrieved
        ↓
Those chunks + the original question are sent to Claude as context
        ↓
Claude reads the chunks and generates an answer
        ↓
Bot replies in Discord with the answer + which PDF/page it came from
```