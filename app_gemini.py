import os
from dotenv import load_dotenv
import google.generativeai as genai
import streamlit as st

# Load environment variables from .env file
load_dotenv()
api_key = os.getenv('API_KEY')

# if "chat_history" not in st.session_state:
#     st.session_state.chat_history = []
#     st.session_state.total_tokens = 0
#     st.session_state.chat = model.start_chat()
# else:
#     chat = st.session_state.chat

# the model settings
sidebar = st.sidebar
sidebar.title("Model Settings")

model = sidebar.selectbox(
    "Model",
    [
        "gemini-1.5-flash",
        "gemini-1.5",
    ],
)

temperature = sidebar.slider(
    "Temperature",
    min_value=0.0,
    max_value=2.0,
    value=1.0,
    step=0.1,
)

genai.configure(api_key=api_key)

generation_config = {
    "temperature": temperature,
    "top_p": 0.95,
    "top_k": 40,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
  model_name=model,
  generation_config=generation_config,
)

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []
    st.session_state.total_tokens = 0
    st.session_state.chat = model.start_chat()
else:
    chat = st.session_state.chat

st.header("Gemini Chat App")

# Display chat history
for message in st.session_state.chat_history:
    with st.chat_message(message["role"]):
        st.write(message["content"])


sidebar.text(f"Total Tokens Used: {st.session_state.total_tokens}/1,000,000")

# Container for text input
input_container = st.container()

# Place the input box in the container
with input_container:
    if prompt := st.chat_input("Enter your message"):
        # Add user message to chat history
        st.session_state.chat_history.append({"role": "user", "content": prompt})
        
        # Get the response from Gemini
        response = st.session_state.chat.send_message(prompt)
        # print(response)
        # print(response.usage_metadata.total_token_count)
        
        # Add assistant response to chat history
        st.session_state.chat_history.append({"role": "assistant", "content": response.text})
        st.session_state.total_tokens = response.usage_metadata.total_token_count
        
        # Rerun to update the chat display
        st.rerun()