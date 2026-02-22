from master_agent import route

print("🤖 Multi-Agent AI System Ready")
print("Type 'exit' to quit")

while True:
    user_input = input("\nYou: ").strip()

    if user_input.lower() == "exit":
        print("Bye 👋")
        break

    response = route(user_input)
    print("\nAI:", response)