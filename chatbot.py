import google.generativeai as genai
import os
from dotenv import load_dotenv

load = load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

genai.configure(api_key=API_KEY)

model = genai.GenerativeModel("gemini-1.5-flash")
chat = model.start_chat(
    history=[
        {"role": "user", "parts": "Hello"},
        {"role": "model", "parts": "Great to meet you. What would you like to know?"},
    ]
)
response = chat.send_message("My Name is Rizwan")
print(response.text)
response = chat.send_message("What is my name?")
print(response.text)


# Output

# Nice to meet you, Rizwan! How can I help you today? 

# Your name is Rizwan!

# Is there anything else I can help you with? 