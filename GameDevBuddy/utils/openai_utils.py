# utils/open_ai.py
import openai
import streamlit as st
from openai import OpenAI

# API key'i Streamlit secrets içinden al
api_key = st.secrets["OPENAI_API_KEY"]
client = OpenAI(api_key=api_key)

def generate_gpt_response(intent: str, user_text: str) -> str:
    """
    GPT-3.5 kullanarak niyete uygun yanıt üretir.
    """
    messages = [
        {"role": "system", "content": "You are a helpful assistant for university students."},
        {"role": "user", "content": f"User intent: {intent}. User's question: {user_text}. Please give a short and clear answer."}
    ]
    
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=messages,
            max_tokens=150,
            temperature=0.3,
        )
        return response.choices[0].message.content.strip()
    
    except Exception as e:
        return f"❌ GPT response error: {e}"
