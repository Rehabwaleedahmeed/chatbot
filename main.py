import requests
from dotenv import load_dotenv
import os
load_dotenv()
api = os.getenv("OPENROUTER_API_KEY")
url = "https://openrouter.ai/api/v1/chat/completions"

headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {api}",
    "HTTP-Referer": "http://localhost"
}

history = [
    {
        "role": "system",
        "content": "You are a helpful, senior software developer. Give clear and concise answers."
    }
]

print(" Chat started (type 'exit' to quit)\n")

while True:
    user_text = input("You: ")

    if user_text.lower() == "exit":
        print("Goodbye")
        break

    history.append({
        "role": "user",
        "content": user_text
    })

    body = {
        "model": "openai/gpt-oss-120b:free",
        "messages": history
    }

    try:
        response = requests.post(url, headers=headers, json=body)
        data = response.json()

        if "error" in data:
            print("Error:", data["error"]["message"])
            continue

        reply = data["choices"][0]["message"]["content"]

        print(f"GPT: {reply}\n")

        history.append({
            "role": "assistant",
            "content": reply
        })

    except Exception as e:
        print("Error:", e)