
import streamlit as st
from datetime import datetime
from zoneinfo import ZoneInfo, ZoneInfoNotFoundError

from langchain_ollama import ChatOllama
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage


# Page configuration
st.set_page_config(
    page_title="My AI Chatbot",
    page_icon="🤖",
    layout="centered",
)

st.title("🤖 My AI Chatbot")
st.caption("Powered by LangChain, Ollama, and Streamlit")


# Initialize the Ollama model
@st.cache_resource
def load_model():
    return ChatOllama(
        model="llama3.2:latest",
        temperature=0,
    )


model = load_model()


# Get the current date and time
def get_current_datetime(timezone="Asia/Karachi"):
    try:
        now = datetime.now(ZoneInfo(timezone))
        return now.strftime(
            "%A, %d %B %Y, %I:%M:%S %p %Z (UTC%z)"
        )
    except (ZoneInfoNotFoundError, ValueError):
        return f"Unknown timezone: {timezone}"


def detect_timezone(question):
    q = question.lower()

    if "london" in q:
        return "Europe/London"
    if "new york" in q:
        return "America/New_York"
    if "tokyo" in q:
        return "Asia/Tokyo"
    if "lahore" in q or "pakistan" in q:
        return "Asia/Karachi"
    if "utc" in q:
        return "UTC"

    return "Asia/Karachi"


def is_datetime_question(question):
    q = question.lower()

    keywords = [
        "time", "date", "today", "right now",
        "current day", "what day", "clock",
    ]

    return any(word in q for word in keywords)


def get_response(question):
    # Use Python directly for current date/time.
    if is_datetime_question(question):
        timezone = detect_timezone(question)
        return get_current_datetime(timezone)

    # Use Ollama for ordinary conversation.
    messages = [
        SystemMessage(
            content=(
                "You are a helpful AI assistant. "
                "Answer clearly and naturally. "
                "Never invent current date or time."
            )
        )
    ]

    for message in st.session_state.chat_history:
        if message["role"] == "user":
            messages.append(HumanMessage(content=message["content"]))
        elif message["role"] == "assistant":
            messages.append(AIMessage(content=message["content"]))

    messages.append(HumanMessage(content=question))

    response = model.invoke(messages)
    return response.content


# Initialize chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []


# Sidebar
with st.sidebar:
    st.header("Settings")
    st.write("Model: `llama3.2:3b`")
    st.write("Runtime: Local Ollama")
    st.write("Default timezone: Asia/Karachi")

    if st.button("Clear chat", use_container_width=True):
        st.session_state.chat_history = []
        st.rerun()


# Display previous messages
for message in st.session_state.chat_history:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])


# Chat input
question = st.chat_input("Ask me anything...")

if question:
    # Show the user message immediately
    st.session_state.chat_history.append(
        {"role": "user", "content": question}
    )

    with st.chat_message("user"):
        st.markdown(question)

    # Generate and display the answer
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            try:
                answer = get_response(question)
                st.markdown(answer)

            except Exception as error:
                answer = (
                    f"Sorry, something went wrong: {error}\n\n"
                    "Check that Ollama is running and the model "
                    "is installed."
                )
                st.error(answer)

    st.session_state.chat_history.append(
        {"role": "assistant", "content": answer}
    )