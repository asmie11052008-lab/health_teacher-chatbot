from ai_utils import ask_ai

def respond(query):
    system_prompt = (
        "You are a study assistant. "
        "Explain concepts clearly, simply, and step by step."
    )
    return ask_ai(system_prompt, query)