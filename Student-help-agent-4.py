#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import streamlit as st
from openai import OpenAI

# Set up OpenAI client with API key from Streamlit secrets
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

st.title("🎓 Student Support Chatbot")
st.write("Ask me anything about your course — syllabus, timings, payments, and more.")

# Chat input from user
user_input = st.chat_input("Type your question here...")

# Display user input and get AI response
if user_input:
    with st.chat_message("user"):
        st.write(user_input)

    with st.spinner("Thinking..."):
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful student support assistant. Answer student queries about course details, schedule, fees, syllabus, and general academic guidance in a friendly and clear manner."},
                {"role": "user", "content": user_input}
            ]
        )

    answer = response.choices[0].message.content

    with st.chat_message("assistant"):
        st.markdown(answer)

