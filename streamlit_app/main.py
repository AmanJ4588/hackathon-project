import streamlit as st
from chat import chat_page
from profile import profile_page
from quiz import quiz_page
from preferences import preferences_page

st.set_page_config(page_title="AI Chatbot", page_icon="🤖", layout="wide")

# Sidebar Navigation
st.sidebar.title("📌 Navigation")
selected_page = st.sidebar.radio("Go to", ["Profile", "Chat", "Quiz", "Preferences"])

# Render the selected page
if selected_page == "Chat":
    chat_page()
elif selected_page == "Profile":
    profile_page()
elif selected_page == "Quiz":
    quiz_page()
elif selected_page == "Preferences":
    preferences_page()
