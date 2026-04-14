# Discord RAG Bot

A Discord bot that answers questions about PDFs using Retrieval-Augmented Generation (RAG). Upload study material PDFs per course and ask questions — the bot fetches relevant content and answers using an LLM.

---

## Project Structure

```
rag-discord-bot/
│
├── bot/
│   ├── __init__.py
│   ├── client.py
│   └── commands/
│       ├── __init__.py
│       ├── upload.py
│       ├── search.py
│       └── list_docs.py
│
├── rag/
│   ├── __init__.py
│   ├── ingestor.py
│   └── retriever.py
│
├── db/
│   ├── __init__.py
│   └── vector_store.py
│
├── storage/
│   └── pdfs/ # where uploaded PDFs are saved locally
│
├── tests/
├── .env
├── .gitignore
├── requirements.txt
├── config.py
└── main.py
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
/upload course:Calc3 + PDF attached
        ↓
Save the PDF file to a local folder
        ↓
Generate a short summary of the PDF using Claude
        ↓
Embed that summary as ONE vector entry with the file path in metadata
        ↓
User asks "I need past Calc 3 finals"
        ↓
ChromaDB finds the most similar PDF summaries
        ↓
Bot sends back the actual PDF files using discord.File()
```