AI-Powered Document Query System

A full-stack web application that allows users to log in, upload documents, and ask questions that are answered strictly using the uploaded content via a controlled Large Language Model (LLM).

This project focuses on functional completeness, backend correctness, and API design, rather than UI aesthetics.

🚀 Features

User authentication (Login / Register)

Document upload (.txt files)

AI-powered question answering using Gemini LLM

Responses constrained strictly to uploaded document content

Graceful handling of out-of-scope queries (no hallucinations)

RESTful API-based backend

Simple, functional frontend

🧱 Tech Stack
Backend

Python

FastAPI

Uvicorn

Gemini LLM API

In-memory database (can be extended to SQL)

Frontend

HTML

CSS

Vanilla JavaScript (Fetch API)

📐 System Architecture
Frontend (HTML + JS)
        |
        | REST API calls
        ↓
Backend (FastAPI - Python)
        |
        | Document storage + Chat handling
        |
        ↓
Gemini LLM (Answer generation)

🔗 API Endpoints
Authentication
POST /register
POST /login

Document Upload
POST /upload-document

Chat
POST /chat