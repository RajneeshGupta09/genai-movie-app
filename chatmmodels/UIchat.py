import streamlit as st
from dotenv import load_dotenv

load_dotenv()

from langchain_mistralai import ChatMistralAI
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage

# Initialize model
model = ChatMistralAI(
    model="mistral-small-2506",
    temperature=1,
    max_tokens=20
)

# Page config
st.set_page_config(page_title="Philosopher Bot", page_icon="🧠")

st.title("🧠 Philosopher Chatbot")
st.write("Talk to a serious philosopher...")

# Initialize chat history in session
if "messages" not in st.session_state:
    st.session_state.messages = [
        SystemMessage(content="you are a serious philosopher")
    ]

# Display previous chat
for msg in st.session_state.messages:
    if isinstance(msg, HumanMessage):
        st.chat_message("user").write(msg.content)
    elif isinstance(msg, AIMessage):
        st.chat_message("assistant").write(msg.content)

# Input box
prompt = st.chat_input("Type your message...")

if prompt:
    # Add user message
    st.session_state.messages.append(HumanMessage(content=prompt))
    st.chat_message("user").write(prompt)

    # Get response
    response = model.invoke(st.session_state.messages)

    # Add AI response
    st.session_state.messages.append(AIMessage(content=response.content))
    st.chat_message("assistant").write(response.content)