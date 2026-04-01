# E-commerce Support Resolution Agent (Multi-Agent RAG)

## Overview
This project implements a multi-agent RAG system using LangChain to resolve customer support tickets using policy documents.

## Features
- Multi-agent pipeline (Triage, Retriever, Writer, Compliance)
- FAISS vector store
- Policy-based responses with citations
- No hallucination enforcement

## Setup

```bash
pip install -r requirements.txt
```

## Run

```bash
python main.py
```

## Input Example
Modify `main.py` with ticket and order context.

## Output
Structured response including:
- Classification
- Decision
- Citations
- Customer response
