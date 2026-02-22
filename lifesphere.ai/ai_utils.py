import requests

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL = "gemma3:4b"

def ask_ai(system_prompt, user_query):
    payload = {
        "model": MODEL,
        "prompt": f"{system_prompt}\nUser: {user_query}\nAI:",
        "stream": False
    }

    try:
        response = requests.post(OLLAMA_URL, json=payload, timeout=500)
        response.raise_for_status()
        return response.json().get("response", "").strip()
    except Exception as e:
        return f"[AI error: {e}]"