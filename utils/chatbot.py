```python
import os
import requests
from dotenv import load_dotenv

load_dotenv()

HF_TOKEN = os.getenv("HF")

API_URL = "https://router.huggingface.co/v1/chat/completions"


def ask_medical_ai(question):

    # TEST: confirms this function is actually being called
    print("CHATBOT FUNCTION CALLED:", question)

    if not HF_TOKEN:
        return "ERROR: HF_TOKEN is missing."

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
                    "You are an AI health assistant. "
                    "Give simple educational information about health and diseases. "
                    "Do not diagnose patients."
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

        print("HF STATUS:", response.status_code)
        print("HF RESPONSE:", response.text)

        if response.status_code != 200:
            return f"Hugging Face API Error: {response.text}"

        result = response.json()

        if "choices" in result:
            return result["choices"][0]["message"]["content"]

        return f"Unexpected API response: {result}"

    except Exception as e:
        return f"AI Error: {str(e)}"
```
