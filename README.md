# Discord-RAG-Bot

### Project Structure
```bash
Discord-RAG-Bot/
│
├── bot/
│   ├── __init__.py
│   ├── client.py          # Discord bot setup & event listeners
│   └── commands/
│       ├── __init__.py
│       ├── upload.py      # /upload command logic
│       ├── ask.py         # /ask command logic
│       └── list_docs.py   # /list command logic
│
├── rag/
│   ├── __init__.py
│   ├── ingestor.py        # PDF parsing & chunking
│   ├── embedder.py        # Turning text into vectors
│   └── retriever.py       # Querying the vector DB + calling LLM
│
├── db/
│   ├── __init__.py
│   └── vector_store.py    # ChromaDB setup & operations
│
├── data/
│   └── chroma/            # Where ChromaDB saves data locally (auto-generated)
│
├── .env                   # Your API keys (never commit this)
├── .gitignore
├── requirements.txt
├── config.py              # Global settings (model names, chunk size, etc.)
└── main.py                # Entry point — runs the bot
```
