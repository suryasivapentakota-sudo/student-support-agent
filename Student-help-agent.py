#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install openai


# In[3]:


# Import libraries
import openai

# Set your OpenAI API key here
openai.api_key = "your-api-key-here"

#Define course information
course_info = {
    "title": "AI for Beginners",
    "schedule": "Tuesdays and Thursdays, 6–7 PM EST",
    "refund": "Full refund within 7 days of payment, minus $10 processing fee.",
    "syllabus": "Introduction to AI, Machine Learning Basics, Neural Networks, Ethics"
}

# Function to build prompt for OpenAI
def build_prompt(question, history=""):
    return f"""
You are a helpful Student Support Agent for an online course.

Course Info:
Title: {course_info['title']}
Schedule: {course_info['schedule']}
Refund Policy: {course_info['refund']}
Syllabus: {course_info['syllabus']}

Conversation History:
{history}

Student Question: {question}

Respond clearly and politely.
"""

# Function to get response from OpenAI
def get_response(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.5
    )
    return response.choices[0].message["content"]

# Chat loop
chat_history = []

while True:
    question = input("You: ")
    if question.lower() in ["exit", "quit"]:
        print("Chatbot: Goodbye!")
        break

    # Build prompt from chat history
    history_text = "\n".join([f"You: {q}\nBot: {a}" for q, a in chat_history])
    prompt = build_prompt(question, history_text)

    # Get and print bot response
    answer = get_response(prompt)
    print("Bot:", answer)

    # Save interaction to history
    chat_history.append((question, answer))


# In[ ]:




