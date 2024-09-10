import google.generativeai as genai
import PIL.Image
import os
from dotenv import load_dotenv

load = load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

genai.configure(api_key=API_KEY)

model = genai.GenerativeModel("gemini-1.5-flash")
# organ = PIL.Image.open(media / "organ.jpg")
organ = PIL.Image.open(os.path.join("img", "cat.jpg"))
response = model.generate_content(["Tell me about this picture", organ])
print(response.text)

# output from model
# The picture shows a cat wearing a brown hat. The cat is sitting on a table with its paws resting on the surface. The cat's eyes are looking at the camera with a serious expression. The cat's fur is brown and grey, and the hat is made of a fuzzy material. The background is blurred, but it appears to be a room with natural light coming in from a window. The picture is well-lit and in focus.
