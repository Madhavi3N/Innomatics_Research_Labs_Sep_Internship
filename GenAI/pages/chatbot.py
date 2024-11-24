import streamlit as st
import google.generativeai as genai


######################
st.snow()
st.image("images/img.png")
st.title('🚀 🤖 Gemini AI Chatbot 💬')
######################


# Reading the API Key and Configuring the API Key
f = open('keys/.gemini_api_key.txt')
key = f.read()
genai.configure(api_key=key)


llm = genai.GenerativeModel("models/gemini-1.5-flash")

chatbot = llm.start_chat(history=[])

st.chat_message("ai").write("Hi there! I am a helpful AI Assistant. How can I help you today?")

human_prompt = st.chat_input("Say Something...")

if human_prompt:
    st.chat_message("human").write(human_prompt)
    response = chatbot.send_message(human_prompt)
    st.chat_message("ai").write(response.text)

