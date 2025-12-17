AI Document Assistant (Full-Stack Project)

A full-stack AI-powered document assistant that allows users to securely log in, upload documents, ask context-aware questions, and generate concise summaries using a Large Language Model (Gemini).

This project demonstrates end-to-end functional completeness, clean API design, frontend–backend integration, and secure AI service usage.

🚀 Features

🔐 User Authentication

Login validation via backend API

📤 Document Upload

Upload text-based documents for processing

💬 Document Q&A

Ask questions strictly based on uploaded content

📝 Document Summarization

Generate concise bullet-point summaries

🔑 Secure API Key Management

LLM API keys managed via environment variables (no secrets in code)

🧠 Why this project?

This system goes beyond a simple chatbot and demonstrates:

Real-world AI-assisted document workflows

Action-based APIs (upload, query, summarize)

Clear separation of frontend and backend concerns

Practical usage of LLMs in an application context

The focus is on functional completeness, as required by the evaluation criteria.

🏗️ Tech Stack
Frontend

HTML

CSS

Vanilla JavaScript

Hosted on Netlify

Backend

Python

FastAPI

REST APIs

Hosted on Render

AI / LLM

Google Gemini API

Securely accessed via environment variables

🔌 API Endpoints
Method	Endpoint	Description
POST	/login	User login validation
POST	/upload-document	Upload a document
POST	/chat	Ask questions about the document
POST	/summarize-document	Generate document summary
GET	/	Backend health check


🔁 Application Flow

User logs in via frontend

Login API validates credentials

User uploads a document

Document is stored in backend memory

User can:

Ask questions based on document content

Generate a structured summary

Backend calls LLM and returns responses

🖱️ Call-To-Actions (CTAs)

Login → triggers authentication API

Upload Document → triggers document ingestion API

Ask → triggers document Q&A API

Generate Summary → triggers summarization API

These CTAs directly map to backend APIs, fulfilling the project requirements.

🔐 Security Practices

❌ No API keys hard-coded in source code

✅ LLM API key loaded via environment variables

✅ .env file excluded from version control

✅ Keys can be rotated without code changes


🛠️ Local Setup
1️⃣ Clone Repository
git clone https://github.com/Shrey-ASC/AI-Document-Chatbot.git
cd AI-Document-Chatbot

2️⃣ Set Environment Variable
setx GEMINI_API_KEY "YOUR_API_KEY"

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Run Backend
uvicorn main:app --reload

5️⃣ Open Frontend

Open index.html or access deployed Netlify URL

Update BACKEND_URL in frontend files if needed
