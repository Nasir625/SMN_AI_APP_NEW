import streamlit as st
import random

st.title("Q&A App")

# 👉 Q&A dictionary (यहीं paste करना है)
qa_dict = {}

topics = ["python", "computer", "ai", "science", "math"]

for i in range(1, 1001):
    topic = random.choice(topics)
    question = f"what is {topic} {i}"
    answer = f"This is answer number {i} about {topic}"
    qa_dict[question] = answer

# 👉 Input box
user_question = st.text_input("Ask me a question!")

# 👉 Button
if st.button("Submit", key="main_btn"):
    answer = qa_dict.get(user_question.lower(), "Answer not found")
    st.write(answer)
