# nutrition_agent.py
from ai_utils import ask_ai

def respond(query):
    system_prompt = (
        "You are a nutrition expert. "
        "Give balanced, practical diet advice."
    )
    return ask_ai(system_prompt, query)