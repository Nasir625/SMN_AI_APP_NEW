import streamlit as st
user_question = st.text_input("Ask me a question!")
import random

# 1000+ questions generate karne ke liye list
qa_dict = {}

topics = ["python", "computer", "ai", "science", "math"]

# 1000 questions generate
for i in range(1, 1001):
    topic = random.choice(topics)
    question = f"what is {topic} {i}"
    answer = f"This is answer number {i} about {topic}"
    qa_dict[question] = answer

# User se question lena
user_question = input("Ask your question: ").lower()
import random

# 1000+ questions generate karne ke liye list
qa_dict = {}

topics = ["python", "computer", "ai", "science", "math"]

# 1000 questions generate
for i in range(1, 1001):
    topic = random.choice(topics)
    question = f"what is {topic} {i}"
    answer = f"This is answer number {i} about {topic}"
    qa_dict[question] = answer

# User se question lena
user_question = input("Ask your question: ").lower()

# Answer dena
if user_question in qa_dict:
    print(qa_dict[user_question])
else:
    print("Answer not found")
# Answer dena
if user_question in qa_dict:
    print(qa_dict[user_question])
else:
    print("Answer not found")
if st.button("Submit"):
    st.write("You asked: ", user_question)
    st.title("SMN_AI🤖")
    st.write(
        "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)
