# environment_agent.py

from ai_utils import ask_ai

def respond(query):
    if query.strip().lower() == "environment":
        query = "Explain an important environmental issue in simple terms."

    system_prompt = (
        "You are an environmental awareness assistant. "
        "Explain environmental topics clearly and responsibly."
    )
    return ask_ai(system_prompt, query)