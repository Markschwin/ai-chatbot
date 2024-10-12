import streamlit as st
import google.generativeai as genai
import pandas as pd
import numpy as np

st.title("🤖 My chatbot app")

gemini_api_key = st.text_input("Gemini API Key: ", placeholder="Type your API Key here...", type="password")
genai.configure(api_key=gemini_api_key)
model = genai.GenerativeModel("gemini-pro")
response = model.generate_content(user_input)
bot_response = response.text


#user input box
#if user_input  := st.text_input("You : ", placeholder = "Type your message here..."):
    #st.write(f"User Input : {user_input}")

#========= Initialize session state for storing chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = [] # Initialize with an empty list

#======== Display all messages 
# using st.write
# for message in st.session_state.chat_history:
#     st.write(f"You : {message}")
for message in st.session_state.chat_history:
    with st.chat_message("user"):
        st.markdown(message)

#========= Display the user input
# if user_input := st.text_input("You: ", placeholder="Type your message here..."):
#     st.session_state.chat_history.append(user_input)
if prompt := st.chat_input("Type your message here ..."):
    st.session_state.chat_history.append(prompt)
    st.chat_message("user").markdown(prompt)
