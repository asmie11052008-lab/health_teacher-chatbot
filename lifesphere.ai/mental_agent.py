# mental_agent.py

from ai_utils import ask_ai

def respond(query):
    system_prompt = (
        "You are a mental health support assistant. "
        "Be calm, empathetic, and practical."
    )
    return ask_ai(system_prompt, query)