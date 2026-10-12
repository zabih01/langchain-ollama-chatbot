
from langchain.agents import create_agent
from langchain_ollama import ChatOllama


# 1. Initialize the Ollama model
model = ChatOllama(
    model="llama3.2:latest",
    temperature=0.7,
)

# 2. Create the chatbot agent without tools
agent = create_agent(
    model=model,
    tools=[],
    system_prompt="""
    You are a helpful AI assistant.

    Instructions:
    - Answer clearly and naturally.
    - Remember information from the conversation history.
    - Use previous messages when answering follow-up questions.
    - If you do not know an answer, say so honestly.
    - Never claim to have performed an action you did not perform.
    """,
)

# 3. Store conversation history
messages = []

print("=" * 50)
print("       LangChain + Ollama Chatbot")
print("=" * 50)
print("Commands:")
print("  exit   - Quit the chatbot")
print("  clear  - Clear conversation history")
print("  help   - Show available commands")
print("=" * 50)
print("Chatbot is ready!\n")


# 4. Main conversation loop
while True:
    try:
        question = input("You: ").strip()

        if not question:
            continue

        # Exit chatbot
        if question.lower() in {"exit", "quit"}:
            print("\nBot: Goodbye! Have a great day.")
            break

        # Clear conversation history
        if question.lower() == "clear":
            messages = []
            print("\nBot: Conversation history cleared.\n")
            continue

        # Show available commands
        if question.lower() == "help":
            print("\nAvailable commands:")
            print("  exit  - Quit the chatbot")
            print("  clear - Clear conversation history")
            print("  help  - Show this help message\n")
            continue

        # 5. Send conversation history to the agent
        result = agent.invoke({
            "messages": messages + [
                {"role": "user", "content": question}
            ]
        })

        # 6. Save the updated conversation history
        messages = result["messages"]

        # 7. Get and display the latest answer
        answer = messages[-1].content

        print(f"\nBot: {answer}\n")

    except KeyboardInterrupt:
        print("\n\nBot: Chatbot stopped.")
        break

    except Exception as e:
        print(f"\nError: {e}")
        print(
            "Check that Ollama is running and "
            "the model is installed.\n"
        )