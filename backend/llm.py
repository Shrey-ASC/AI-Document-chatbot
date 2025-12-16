import os
import requests
import logging

logger = logging.getLogger(__name__)

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

if not GEMINI_API_KEY:
    raise RuntimeError("GEMINI_API_KEY environment variable not set")

GEMINI_URL = (
    "https://generativelanguage.googleapis.com/v1beta/"
    "models/gemini-2.5-flash-lite:generateContent"
)

def call_gemini(prompt: str) -> str:
    payload = {
        "contents": [
            {
                "parts": [{"text": prompt}]
            }
        ]
    }

    try:
        r = requests.post(
            f"{GEMINI_URL}?key={GEMINI_API_KEY}",
            headers={"Content-Type": "application/json"},
            json=payload,
            timeout=30
        )

        if r.status_code != 200:
            logger.error(f"Gemini API error {r.status_code}: {r.text}")
            return "LLM service error."

        data = r.json()

        return (
            data.get("candidates", [{}])[0]
                .get("content", {})
                .get("parts", [{}])[0]
                .get("text", "Not available.")
        )

    except Exception as e:
        logger.error(f"LLM error: {e}")
        return "LLM processing error."


def ask_llm(context: str, question: str) -> str:
    prompt = f"""Answer ONLY using the content below.
If the answer is not found, say: Not available in the document.

Document:
{context}

Question:
{question}
"""
    return call_gemini(prompt)


def summarize_document(context: str) -> str:
    prompt = f"""Summarize the following document in 5–7 clear bullet points.
Be concise and factual.

Document:
{context}
"""
    return call_gemini(prompt)
