import streamlit as st
import google.generativeai as genai

# Reading the API Key and Configuring the API Key
f = open('keys/.gemini_api_key.txt')
key = f.read()
genai.configure(api_key=key) 

######################
st.snow()
st.image("images/img.png")
st.title("🤖 GenAI App - AI Code Reviewer")
######################

llm = genai.GenerativeModel("models/gemini-1.5-flash")
chatbot = llm.start_chat(history=[])

if "chat_history" not in st.session_state:
    st.session_state["chat_history"] = []

def update_chat(role, message):
    st.session_state["chat_history"].append({"role": role, "content": message})

input_code = st.text_area("Paste your Python code here:", height=200)

# Button for code review
if st.button("Review Code"):
    st.balloons()
    if input_code.strip():
        update_chat("human", input_code)
        review_prompt = f"Review the following Python code. Identify bugs, areas of improvement, and provide fixed code snippets:\n{input_code}"
        response = chatbot.send_message(review_prompt)
        
        # Add AI response to chat history and display
        update_chat("ai", response.text)
        st.success("Code reviewed successfully! See suggestions below.")
        st.subheader("AI Suggestions and Fixed Code:")
        st.write(response.text)
    else:
        st.warning("Please paste some Python code to review.")


# Button to view past history
if st.button("Show History"):
    st.balloons()
    if st.session_state["chat_history"]:
        st.subheader("Past Review History")
        for entry in st.session_state["chat_history"]:
            role = "User" if entry["role"] == "human" else "AI"
            st.markdown(f"**{role}:** {entry['content']}")
    else:
        st.info("No history available yet.")
