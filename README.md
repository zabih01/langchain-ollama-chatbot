# 🤖 LangChain Ollama Chatbot

**A simple, extensible, and fully local AI chatbot built with Python, LangChain, Ollama, and uv.**

Chat with a locally running large language model through an interactive terminal interface. Maintain conversation context, ask follow-up questions, and experiment with building AI applications without relying on paid cloud APIs.

## ✨ Features

- **Local AI Inference** — Run language models locally using Ollama.
- **Conversational Memory** — Maintain context across messages within a session.
- **LangChain Integration** — Build on LangChain's agent framework.
- **Custom System Prompt** — Configure the assistant's behavior and response style.
- **Simple CLI Interface** — Interact with the chatbot directly from your terminal.
- **Clear Conversation** — Reset conversation history with a simple command.
- **Error Handling** — Handle common runtime errors and keyboard interruptions.
- **Modern Python Workflow** — Manage dependencies and project environments with `uv`.

## 🛠️ Tech Stack

| Technology                              | Purpose                                        |
| --------------------------------------- | ---------------------------------------------- |
| Python                                  | Core programming language                      |
| [LangChain](https://www.langchain.com/) | Agent framework and conversation orchestration |
| [Ollama](https://ollama.com/)           | Local LLM runtime                              |
| [uv](https://docs.astral.sh/uv/)        | Dependency and project management              |

## 📋 Prerequisites

Before getting started, make sure you have:

- Python installed.
- `uv` installed and available in your terminal.
- Ollama installed and running.
- The `llama3.2:latest` model downloaded.

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/langchain-ollama-chatbot.git
cd langchain-ollama-chatbot
```

### 2. Install dependencies

```bash
uv sync
```

### 3. Download the Ollama model

```bash
ollama pull llama3.2:latest
```

### 4. Run the chatbot

```bash
uv run main.py
```

That's it! Your local AI chatbot is ready to use.

## 💬 Example Conversation

```text
==================================================
       LangChain + Ollama Chatbot
==================================================
Commands:
  exit   - Quit the chatbot
  clear  - Clear conversation history
  help   - Show available commands
==================================================
Chatbot is ready!

You: My favorite language is Python.

Bot: Python is a great choice! What do you enjoy
about programming with it?

You: What is my favorite language?

Bot: Your favorite programming language is Python.
```

_Responses will vary depending on the model and conversation._

## ⌨️ Available Commands

| Command | Description                            |
| ------- | -------------------------------------- |
| `help`  | Display available commands             |
| `clear` | Clear the current conversation history |
| `exit`  | Exit the chatbot                       |

## 📁 Project Structure

```text
langchain-ollama-chatbot/
├── main.py          # Chatbot application
├── pyproject.toml   # Project metadata and dependencies
├── uv.lock          # Locked dependency versions
├── .gitignore       # Files excluded from Git
└── README.md        # Project documentation
```

## 🧠 How It Works

1. **User Input:** The chatbot receives a message from the terminal.
2. **Context Management:** Previous messages are included to support follow-up questions.
3. **Agent Execution:** LangChain passes the conversation to the configured Ollama model.
4. **Response Generation:** The model generates a response locally.
5. **History Update:** The conversation is retained in memory for the current session.

## 🔒 Privacy and Limitations

- Model inference runs locally through Ollama.
- No external LLM API key is required for the basic chatbot.
- Conversation history is stored in memory and is cleared when the program exits.
- The chatbot does not have permanent memory, web search, or external tools enabled by default.
- Model performance depends on your hardware and the selected Ollama model.

## 🗺️ Future Improvements

Potential extensions for this project include:

- [ ] Streaming responses
- [ ] Persistent conversation history using SQLite
- [ ] Retrieval-Augmented Generation (RAG) for PDFs and documents
- [ ] Custom tools and external API integrations
- [ ] Streamlit-based web interface
- [ ] Configurable model selection
- [ ] Automated tests and improved logging

## 🤝 Contributing

Contributions, suggestions, and improvements are welcome.

1. Fork the repository.
2. Create a feature branch.
3. Commit your changes.
4. Open a pull request.

## 📄 License

Choose a license before distributing this project. For example, an MIT License allows broad reuse with attribution; add a `LICENSE` file if you choose MIT.

---

**Built to explore local AI, LangChain agents, and practical LLM application development.**
