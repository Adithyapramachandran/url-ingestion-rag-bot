# url-ingestion-rag-bot
# RAG-Based Recursive Website Chatbot (API-Free)

## Project Overview

This project implements a Retrieval-Augmented Generation (RAG) chatbot that ingests a user-provided website URL, recursively scrapes relevant content from linked pages, and answers user questions strictly based on the collected website data.

The system operates entirely without external API keys by leveraging local embedding models and a local language model.

---

## Key Features

- Recursive website scraping
- Structured and unstructured content handling
- Text chunking with overlap
- Local embedding generation (SentenceTransformers)
- FAISS-based vector similarity search
- Local LLM answer generation (Flan-T5)
- React-based demo UI
- Source citation display
- No external API dependency

---

## System Architecture

1. User provides website URL.
2. Recursive scraper collects internal pages.
3. Text is cleaned and chunked.
4. Chunks are converted into embeddings.
5. Embeddings are stored in FAISS.
6. User question is embedded.
7. Top-k similar chunks are retrieved.
8. Local LLM generates grounded answer.

---

## Setup Instructions

### Option 1: Run via Google Colab

Open `notebook/demo_colab.ipynb` and execute all cells.

### Option 2: Run Locally

1. Clone the repository:

