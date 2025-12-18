import streamlit as st
from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

client = genai.Client(api_key = os.getenv("GEMINI_API_KEY"))


# messages = [
#     {
#         "role":"AI",
#         "content": "Hello! How can I assit you today?"
#     },
#     {
#         "role": "AI",
#         "content": " Can you tell me a joke?"
#     },
#     {
#         "role": " AI",
#         "content": "Sure! Why did that scarecrow win an award? Because he was outstanding in his field! "
#     }
# ]

if "messages" not in st.session_state:
    st.session_state.messages = [{
        "role": " AI",
        "content": "😍 Hello! How can I assist you today?" 
        }]

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])
        
user_input = st.chat_input("Enter your message here...")

if user_input:
    st.session_state.messages.append({
        "role":"User",
        "content": user_input
    })
    
    with st.chat_message("User"):
        st.markdown(user_input)
        
    response = client.models.generate_content(
    model = "gemini-2.5-flash",
    contents = list(map(lambda message: message["role"] + ": "+ message["content"], st.session_state.messages ))
    )
    
    st.session_state.messages.append({
        "role":"ai",
        "content":response.text
    })
    
    with st.chat_message("ai"):
        st.markdown(response.text)