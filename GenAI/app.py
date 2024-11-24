import streamlit as st
import google.generativeai as genai

######################
st.balloons()
st.image("images/img.png")
st.title("🚀 🤖 Data Science Tutor Application")
######################

# Reading the API Key and Configuring the API Key
f = open('keys/.gemini_api_key.txt')
key = f.read()
genai.configure(api_key=key)

sys_prompt = """You are a helpful AI Tutor for Data Science. 
                Students will ask you doubts related to various topics in data science.
                You are expected to reply in as much detail as possible. 
                Make sure to take examples while explaining a concept.
                In case if a student ask any question outside the data science scope, 
                politely decline and tell them to ask the question from data science domain only."""

model = genai.GenerativeModel(model_name="models/gemini-1.5-flash", 
                          system_instruction=sys_prompt)


user_prompt = st.text_input("Enter your query:", placeholder="Type your query here...")

btn_click = st.button("Generate Answer")

if btn_click==True:
    # do something
    st.snow()
    st.balloons()
    # generate respose: we need gemini or gpt model, configure (set the api key), call the model to generate the response
    response = model.generate_content(user_prompt)
    st.write(response.text)