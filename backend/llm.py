import requests
import logging

logger = logging.getLogger(__name__)

GEMINI_API_KEY = "AIzaSyAo77PVosRpiSsSosIp_JE_Kol5ALB0YiE"

GEMINI_URL = (
    "https://generativelanguage.googleapis.com/v1beta/"
    "models/gemini-2.5-flash-lite:generateContent"
)

def ask_llm(context, question):
    prompt = f"""Answer ONLY using the content below.
If the answer is not found, say: Not available in the document.

Document:
{context}

Question:
{question}
"""

    payload = {
        "contents": [
            {
                "parts": [
                    {"text": prompt}
                ]
            }
        ]
    }

    headers = {
        "Content-Type": "application/json"
    }

    try:
        r = requests.post(
            f"{GEMINI_URL}?key={GEMINI_API_KEY}",
            headers=headers,
            json=payload,
            timeout=30
        )

        # 1️⃣ HTTP failure
        if r.status_code != 200:
            logger.error(f"Gemini API error {r.status_code}: {r.text}")
            return "LLM service error."

        # 2️⃣ Empty response
        if not r.text.strip():
            logger.error("Gemini returned empty response")
            return "LLM returned no response."

        # 3️⃣ JSON parse
        data = r.json()

        # 4️⃣ Safe extraction
        return (
            data.get("candidates", [{}])[0]
                .get("content", {})
                .get("parts", [{}])[0]
                .get("text", "Not available in the document.")
        )

    except requests.exceptions.RequestException as e:
        logger.error(f"Request failed: {e}")
        return "LLM connection error."

    except Exception as e:
        logger.error(f"Unexpected LLM error: {e}")
        return "LLM processing error."
