import requests
from dotenv import load_dotenv
load_dotenv()
HF_TOKEN ="HF"

API_URL = "https://router.huggingface.co/v1/chat/completions"



headers = {
    "Authorization": f"Bearer {HF_TOKEN}",
    "Content-Type": "application/json"
}


def ask_medical_ai(question):

    payload = {
        "model": "meta-llama/Llama-3.1-8B-Instruct",
        "messages": [
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

        print("Status:", response.status_code)
        print(response.text)

        result = response.json()

        if "choices" in result:
            return result["choices"][0]["message"]["content"]

        elif "error" in result:
            return result["error"]

        else:
            return str(result)

    except Exception as e:
        return str(e)
print(ask_medical_ai("Explain SQL injection vulnerability and prevention"))