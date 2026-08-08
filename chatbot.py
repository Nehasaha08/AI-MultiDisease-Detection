```python
import os
import requests
from dotenv import load_dotenv

load_dotenv()

HF_TOKEN = os.getenv("HF_TOKEN")

API_URL = "https://router.huggingface.co/v1/chat/completions"

def ask_medical_ai(question):

    if not HF_TOKEN:
        return "AI assistant is not configured. Please add HF_TOKEN to Streamlit Secrets."

    headers = {
        "Authorization": f"Bearer {HF_TOKEN}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": "meta-llama/Llama-3.1-8B-Instruct",
        "messages": [
            {
                "role": "system",
                "content": (
                    "You are an AI health assistant for an educational medical "
                    "image detection application. Give clear, simple and helpful "
                    "health information. Do not claim to diagnose a patient. "
                    "For serious symptoms, recommend consulting a qualified doctor."
                )
            },
            {
                "role": "user",
                "content": question
            }
        ],
        "max_tokens": 300,
        "temperature": 0.5
    }

    try:
        response = requests.post(
            API_URL,
            headers=headers,
            json=payload,
            timeout=60
        )

        if response.status_code != 200:
            try:
                error_data = response.json()
                return f"AI service error: {error_data.get('error', error_data)}"
            except Exception:
                return f"AI service error: HTTP {response.status_code}"

        result = response.json()

        if "choices" in result and result["choices"]:
            return result["choices"][0]["message"]["content"]

        return "The AI assistant did not return a response."

    except requests.exceptions.Timeout:
        return "The AI assistant took too long to respond. Please try again."

    except requests.exceptions.RequestException as e:
        return f"Connection error: {str(e)}"

    except Exception as e:
        return f"AI assistant error: {str(e)}"
```
