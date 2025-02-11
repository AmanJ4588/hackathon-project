import streamlit as st
import requests


def chat_page(): 
    # Initialize chat history in the correct format
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Display chat history
    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):  
            st.write(msg["parts"][0]["text"])  # Extract text from 'parts'

    # Get user input
    user_input = st.chat_input("Ask me Anything...")

    if user_input:
        # Display user input immediately
        with st.chat_message("user"):
            st.write(user_input)

        # Store in correct Gemini format
        st.session_state.messages.append({"role": "user", "parts": [{"text": user_input}]})

        # Send request to Flask backend
        response = requests.post("http://127.0.0.1:5000/chat", json={"messages": st.session_state.messages})

        if response.status_code == 200:
            bot_reply = response.json().get("response", "Error getting response")

            # Store bot's reply in correct format
            st.session_state.messages.append({"role": "model", "parts": [{"text": bot_reply}]})

            with st.chat_message("model"):
                st.write(bot_reply)
