#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import streamlit as st
import openai

st.title("🎓 Student Support Chatbot")

openai.api_key = st.secrets["OPENAI_API_KEY"]

user_input = st.chat_input("Ask a question about your course")

if user_input:
    with st.spinner("Getting answer..."):
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful student support assistant."},
                {"role": "user", "content": user_input}
            ]
        )
        st.markdown("**Answer:** " + response.choices[0].message["content"])

