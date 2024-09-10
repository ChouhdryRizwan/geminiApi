import google.generativeai as genai
import os
from dotenv import load_dotenv

load = load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

genai.configure(api_key=API_KEY)

model = genai.GenerativeModel("gemini-1.5-flash")
response = model.generate_content("Write a story about a magic backpack.", stream=True)
for chunk in response:
    print(chunk.text)
    print("_" * 80)
    

# Output    
# Elara, a girl with hair the color of a stormy sky and eyes like melted
# ________________________________________________________________________________
#  chocolate, lived a life filled with daydreams. Every day, she’d
# ________________________________________________________________________________
#  escape into the pages of her worn out adventure books, dreaming of faraway lands and daring quests. She wished for a world beyond the dusty streets of her village
# ________________________________________________________________________________
# , a world where she could be the hero, not just the reader. 

# One day, while rummaging through her attic, Elara stumbled upon
# ________________________________________________________________________________
#  a dusty, leather backpack tucked behind a pile of old trunks. It was intricately embroidered with strange symbols, and when she touched it, a warmth spread through her fingertips. A whisper, faint but clear, echoed in her mind, "
# ________________________________________________________________________________
# Adventure awaits, Elara."

# Elara, though a little scared, couldn’t resist the pull of the whisper. She slung the backpack over her shoulder and stepped outside. As she did, the world around her shimmered,
# ________________________________________________________________________________
#  the mundane streets transforming into a vibrant jungle teeming with exotic plants and vibrant birds. The backpack, as if sensing her surprise, unzipped itself, revealing a shimmering portal within. 

# "This is your first adventure, Elara," the whisper returned. It wasn't a voice, exactly, but a feeling,
# ________________________________________________________________________________
#  a comforting guide. 

# With a nervous breath, Elara stepped through the portal. She found herself in a fantastical land, a place straight out of her beloved stories. Lush forests stretched before her, populated by talking animals and mischievous fairies. A crystal river glittered under the sun, and towering waterfalls cascaded
# ________________________________________________________________________________
#  into emerald pools.

# Elara explored this world, the magic backpack her constant companion. It seemed to know her every need. When she was thirsty, it filled with cool, refreshing water. When she needed a warm blanket, it produced one, woven from moonbeams. It even provided a sturdy sword when she encountered
# ________________________________________________________________________________
#  a grumpy troll guarding a hidden path. 

# Each day, the backpack offered a new challenge, a new puzzle, a new adventure. Elara befriended a fire-breathing dragon, helped a mischievous pixie retrieve her lost wings, and even climbed a mountain that touched the clouds.

# But most importantly, she
# ________________________________________________________________________________
#  discovered a strength within herself she didn’t know she possessed. She learned courage, resilience, and the power of kindness. Each adventure, each challenge, chipped away at the fear and uncertainty, leaving her bolder, brighter, and 
# stronger.

# One day, she felt the pull of home. The whisper in her
# ________________________________________________________________________________
#  mind guided her back through the portal, back to the familiar streets of her village. She returned, not the same girl who had left. She was a changed person, filled with stories and experiences, a fire in her eyes that shone brighter than the sun.

# Elara knew this was just the beginning. The magic
# ________________________________________________________________________________
#  backpack, a constant reminder of her adventures, sat nestled in her room, waiting for the next whisper, the next adventure. She was ready. The world, she knew, was just waiting to be explored. 

# ________________________________________________________________________________    