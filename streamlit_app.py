import streamlit as st
user_question = st.text_input("Ask me a question!")
import random
# Sawal aur Jawab ki list
knowledge_base = {
    "computer kya hai": "Computer ek electronic machine hai jo data process karti hai.",
    "cpu kya hai": "CPU computer ka dimaag hota hai, ise Central Processing Unit kehte hain.",
    "ram ka full form kya hai": "RAM ka full form Random Access Memory hai.",
    "bharat ki rajdhani kya hai": "Bharat ki rajdhani New Delhi hai.",
    "2+2 kitna hota hai": "2+2 ka jawab 4 hai."
}

# Button dabne par jawab dikhane ka logic
if st.button("Submit"):
    # Sawal ko chote letters mein badalna taaki match ho sake
    query = user_question.lower().strip()
    
    if query in knowledge_base:
        st.success(f"Jawab: {knowledge_base[query]}")
    else:
        st.warning("Maaf kijiyega, mujhe iska jawab nahi pata. Par main seekh raha hoon!")

if st.button("Submit"):
    st.write("You asked: ", user_question)
    st.title("SMN_AI🤖")
    st.write(
        "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)
