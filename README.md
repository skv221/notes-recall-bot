# Notes Recall Bot

A personal RAG-based chatbot that helps me recollect what I've learned from my notes.

Instead of manually searching through multiple learning notes, Notes Recall Bot retrieves relevant chunks from my notes and uses Gemini to generate grounded answers based only on the retrieved information.

---

## Features

- Recursively loads notes from folders and subfolders
- Supports Markdown and text files
- Splits documents into configurable chunks
- Uses overlapping chunks to preserve context
- Generates embeddings for document chunks
- Stores embeddings persistently using ChromaDB
- Performs semantic similarity search
- Uses Gemini for response generation
- Keeps responses grounded in retrieved notes
- Provides source citations
- Modular Python project structure

---

## Architecture

    Notes
      |
      v
    Document Loader
      |
      v
    Document Chunker
      |
      v
    Embedding Generation
      |
      v
    ChromaDB
      |
      v
    Semantic Search
      |
      v
    Relevant Chunks
      |
      v
    Gemini
      |
      v
    Grounded Answer
      |
      v
    Source Citation

---

## Project Structure

    notes-recall-bot/
    |
    +-- app.py
    |
    +-- notes/
    |   +-- Week 1 Notes/
    |   +-- Week 2 Notes/
    |   +-- Week 3 Notes/
    |
    +-- ingestion/
    |   +-- loader.py
    |   +-- chunker.py
    |   +-- embedding.py
    |
    +-- retrieval/
    |   +-- search.py
    |
    +-- generation/
    |   +-- llm.py
    |
    +-- chroma_db/
    |
    +-- .env
    +-- .gitignore
    +-- requirements.txt
    +-- README.md

---

## How It Works

### 1. Document Loading

Notes are recursively loaded from the `notes` directory.

Markdown and text files inside nested folders are supported.

For example:

    notes/
    |
    +-- Python/
    |   +-- asyncio.md
    |   +-- pydantic.md
    |
    +-- FastAPI/
    |   +-- fastapi.md
    |
    +-- RAG/
        +-- chromadb.md

---

### 2. Document Chunking

Documents are divided into smaller chunks before generating embeddings.

Current configuration:

- Chunk size: 125 words
- Chunk overlap: 20 words

The overlap helps preserve context between consecutive chunks.

The effective step between chunks is:

    125 - 20 = 105 words

---

### 3. Embedding Generation

Each chunk is converted into a vector representation using an embedding model.

    Text Chunk
        |
        v
    Embedding Model
        |
        v
    Vector Embedding

---

### 4. Persistent ChromaDB

The generated embeddings are stored in ChromaDB using persistent storage.

    Notes
      |
      v
    Chunks
      |
      v
    Embeddings
      |
      v
    ChromaDB
      |
      v
    Persistent Storage

This allows the vector database to remain available between application runs.

---

### 5. Semantic Search

When a question is asked, the query is converted into an embedding and compared with the stored embeddings.

    "What is Pydantic?"
            |
            v
      Query Embedding
            |
            v
      Similarity Search
            |
            v
      Relevant Chunks

---

### 6. Gemini Response Generation

The retrieved chunks are provided to Gemini along with the user's question.

The model is instructed to:

- Answer using only the retrieved notes
- Understand and synthesize the retrieved information
- Explain the answer in its own words
- Combine relevant chunks when necessary
- Avoid inventing information
- Mention when the notes don't contain enough information
- Cite the relevant source metadata

---

## Example

    > What is Pydantic?

    Bot is recollecting 'What is Pydantic?'.....

    Bot:
    Pydantic is a Python library used for validating and structuring
    data using Python type hints. It performs runtime validation and
    can also handle parsing and serialization.

    Sources:
    - Pydantic and Type Hints.md

---

## Technologies Used

- Python
- Google Gemini API
- ChromaDB
- Embeddings
- Retrieval-Augmented Generation (RAG)
- pathlib
- python-dotenv

---

## Setup

### 1. Clone the Repository

    git clone <your-repository-url>
    cd notes-recall-bot

### 2. Create a Virtual Environment

    python -m venv venv

Activate it on Windows:

    venv\Scripts\activate

### 3. Install Dependencies

    pip install -r requirements.txt

### 4. Configure the Gemini API Key

Create a `.env` file:

    GEMINI_API_KEY=your_api_key_here

### 5. Add Your Notes

Place your learning notes inside the `notes` directory.

Nested folders are supported.

### 6. Run the Application

    python app.py

---

## What I Learned

This project helped me understand how the components of a RAG application work together:

    Documents
        |
        v
    Ingestion
        |
        v
    Chunking
        |
        v
    Embeddings
        |
        v
    Vector Database
        |
        v
    Semantic Retrieval
        |
        v
    Relevant Context
        |
        v
    LLM
        |
        v
    Grounded Response

Key concepts explored:

- Document ingestion
- Recursive file discovery
- Text chunking
- Chunk overlap
- Embeddings
- Vector databases
- Persistent ChromaDB
- Semantic similarity search
- Retrieval-Augmented Generation
- Prompt engineering
- Grounded LLM responses
- Source attribution
- Modular Python architecture

---

## Project Goal

The goal of Notes Recall Bot is simple:

> Turn everything I've learned into something I can talk to.

Instead of manually searching through my learning notes, I can ask questions naturally and let the RAG pipeline retrieve the relevant knowledge for me.

---

## Author

**V**

Built as part of my journey learning Agentic AI, RAG, embeddings, vector databases, and LLM application development with Python.