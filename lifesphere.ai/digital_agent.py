# digital_agent.py

from ai_utils import ask_ai

def respond(question):
    prompt = f"You are a digital technology assistant.\nQuestion: {question}"
    return ask_ai(prompt)