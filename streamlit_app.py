import streamlit as st
import google.generativeai as genai
from PIL import Image
import os

# --- Page Configuration ---
st.set_page_config(page_title="SMN AI Assistant 2.0", page_icon="🤖", layout="wide")

# --- UI Styling (Dark Theme & Professional Look) ---
st.markdown("""
    <style>
    .main { background-color: #1a1a2e; color: white; }
    .stTextInput > div > div > input { background-color: #16213e; color: white; }
    .stChatInputContainer { position: fixed; bottom: 20px; z-index: 1000; width: 80%; left: 10%;}
    </style>
    """, unsafe_allow_html=True)

# --- Sidebar for Settings ---
with st.sidebar:
    st.title("⚙️ AI Control Panel")
    st.markdown("---")
    
    # API Key Input
    api_key = st.text_input("Gimme your Google API Key:", type="password")
    
    st.markdown("---")
    # File Uploader for Images
    uploaded_file = st.file_uploader("📷 Photo Analyze karein (optional)", type=["jpg", "jpeg", "png"])
    
    if uploaded_file:
        # Display the uploaded image
        image = Image.open(uploaded_file)
        st.image(image, caption='Aapki Uploaded Photo', use_container_width=True)
    
    st.markdown("---")
    # Clear Chat Button
    if st.button("🗑️ Clear Chat History"):
        st.session_state.messages = []
        # Clear the uploaded file implicitly on refresh or manually
        st.rerun()

# --- AI Model Setup ---
if api_key:
    try:
        genai.configure(api_key=api_key)
        # We use Gemini 1.5 Flash for multimodal (text + images) tasks
        model = genai.GenerativeModel('gemini-1.5-flash')
    except Exception as e:
        st.error(f"Error configuring AI: {e}")
else:
    st.warning("Please enter your API Key in the sidebar to start.")

# --- Chat Logic (State Management) ---
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history on app reload
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# --- Main Interaction Logic ---
# Input box at the bottom
if prompt := st.chat_input("Prompt likhein yahan... (e.g., 'Is photo mein kya hai?')"):
    
    # 1. Store and show user message
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # 2. Process AI Response
    if not api_key:
        st.error("Pehle API key daalein!")
    else:
        with st.chat_message("assistant"):
            message_placeholder = st.empty()
            full_response = ""
            
            try:
                content_list = []
                content_list.append(prompt) # Add user text
                
                # Check if image is uploaded
                if uploaded_file:
                    image_data = Image.open(uploaded_file)
                    content_list.append(image_data) # Add image data
                
                # Generate content (Multimodal)
                response = model.generate_content(content_list, stream=True)
                
                # Streaming output
                for chunk in response:
                    # In some rare cases chunk.text can fail if there's an issue with the generation
                    if chunk.text:
                        full_response += chunk.text
                        message_placeholder.markdown(full_response + "▌")
                    else:
                        full_response += "(No text response)"
                
                message_placeholder.markdown(full_response)
                
                # Store assistant response in history
                st.session_state.messages.append({"role": "assistant", "content": full_response})
                
            except Exception as e:
                st.error(f"Something went wrong: {e}")
        
