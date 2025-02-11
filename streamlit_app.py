import streamlit as st
from query_data import RAGChatbot

chatbot = RAGChatbot()

st.set_page_config(page_title="RAG Chatbot", layout="wide")
st.title("Troubleshooting chatbot")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

query_text = st.text_input("How can I help you?", key="user_query")

if query_text:
    response_text, sources = chatbot.query(query_text)

    st.session_state.chat_history.append({"role":"user","text":query_text})
    st.session_state.chat_history.append({"role":"assistant","text":response_text,"sources":sources})

#st.subheader("Chat History")
for chat in st.session_state.chat_history:
    with st.chat_message("user" if chat["role"]=="user" else "assistant"):
        st.write(chat["text"])
        if chat["role"]=="assistant" and chat["sources"]:
            st.write(f"📌 **Sources:** {', '.join(filter(None, chat['sources']))}")

    

