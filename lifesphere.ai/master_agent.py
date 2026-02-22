from study_agent import respond as study
from mental_agent import respond as mental
from fitness_agent import respond as fitness
from nutrition_agent import respond as nutrition
from environment_agent import respond as environment
from ai_utils import ask_ai

def route(query):
    q = query.lower().strip()

    if "study" in q:
        return study(query)

    elif "mental" in q or "stress" in q or "anxiety" in q:
        return mental(query)

    elif "fitness" in q or "workout" in q:
        return fitness(query)

    elif "nutrition" in q or "diet" in q:
        return nutrition(query)

    elif "environment" in q or "climate" in q:
        return environment(query)

    # ✅ DEFAULT: ALWAYS CALL OLLAMA
    else:
        system_prompt = (
            "You are a general-purpose AI assistant. "
            "Answer clearly and helpfully."
        )
        return ask_ai(system_prompt, query)