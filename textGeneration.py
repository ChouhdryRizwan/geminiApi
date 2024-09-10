import google.generativeai as genai
import os
from dotenv import load_dotenv

load = load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

genai.configure(api_key=API_KEY)

# model = genai.GenerativeModel("gemini-1.5-flash")
# response = model.generate_content("Write a story about a magic backpack.")
model = genai.GenerativeModel("gemini-1.5-flash",system_instruction="You are a expert doctor.")
response = model.generate_content("I have pain in my knee")
print(response.text)



#output

# I understand you're experiencing knee pain, but I am an AI and cannot provide medical advice. To help you, I need more information:

# **Please tell me:**

# * **Where exactly in your knee is the pain located?** (e.g., front, back, inside, outside)
# * **What kind of pain is it?** (e.g., sharp, dull, aching, throbbing)
# * **When did the pain start?**
# * **What makes the pain worse?** (e.g., standing, walking, sitting)
# * **What makes the pain better?** (e.g., rest, ice, medication)
# * **Do you have any other symptoms?** (e.g., swelling, stiffness, redness)
# * **Have you had any recent injuries?**
# * **Have you had any previous knee problems?**

# **It is important to seek professional medical advice from a doctor or qualified healthcare provider for any
# **It is important to seek professional medical advice from a doctor or qualified healthcare provider for any pain or discomfort you experience. They can properly diagnose the cause of your pain and recommend the best treatment options.**


# **In the meantime, you can try the RICE method (Rest, Ice, Compression, Elevation) to help manage the pain and swelling.**

# Remember, self-diagnosis can be dangerous. Please consult a medical professional for proper diagnosis and treatment.


