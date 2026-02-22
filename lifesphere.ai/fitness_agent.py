# fitness_agent.py

from ai_utils import ask_ai

def respond(query):
    system_prompt = (
        "You are a fitness coach. "
        "Give safe, realistic workout and health advice."
    )
    return ask_ai(system_prompt, query)