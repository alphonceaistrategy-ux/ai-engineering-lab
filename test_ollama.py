import requests

OLLAMA_URL = "http://localhost:11434/api/generate"

def ask_ollama(prompt):
    response = requests.post(
        OLLAMA_URL,
        json={
            "model": "llama3.2:1b",
            "prompt": prompt,
            "stream": False
        }
    )

    response.raise_for_status()
    data = response.json()
    return data["response"]

print("AI READY (Ollama connected)\n")

while True:
    user_input = input("You: ")

    if user_input.lower() in ["exit", "quit"]:
        break

    answer = ask_ollama(user_input)
    print("\nAI:", answer, "\n")