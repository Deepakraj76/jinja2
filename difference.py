from jinja2 import Template
import google.generativeai as genai

# Load environment variables
genai.configure(api_key="AIzaSyC-onsUqc_veajLrXKnr5g3iUJiduyTnQg")

# Zero-Shot Prompting (No examples)
zero_shot_template_string = """
Summarize the following text:

"The Eiffel Tower, built in 1889 as the entrance arch to 
the 1889 World's Fair, is one of the most recognizable structures in the world. 
Standing 324 meters tall, it was the tallest man-made structure in the world for 41 years
until the completion of the Chrysler Building in New York City. 
The Eiffel Tower is named after the engineer Gustave Eiffel, whose company designed and built the tower. 
It is a global cultural icon of France and one of the most-visited paid monuments in the world, with 
millions of visitors every year."
"""

# Few-Shot Prompting (With examples)
few_shot_template_string= """
Here are some examples of summarizing text into subtopics:

Example 1:
Original: "The Mona Lisa is a famous painting created by Leonardo da Vinci. It is considered one of the most valuable pieces of art in the world, and is housed in the Louvre Museum in Paris."
Summary:
- Artwork: "The Mona Lisa is a world-famous painting created by Leonardo da Vinci."
- Location: "It is housed in the Louvre Museum, Paris."
- Value: "It is considered one of the most valuable artworks in the world."

Example 2:
Original: "Mount Everest, located in the Himalayas, is the tallest mountain in the world, standing at 8,848 meters above sea level. It attracts climbers from all over the world."
Summary:
- Location: "Mount Everest is located in the Himalayas."
- Height: "It stands at 8,848 meters, making it the tallest mountain in the world."
- Attraction: "Mount Everest attracts climbers from all over the world."

Now, summarize the following text:

"The Eiffel Tower, built in 1889 as the entrance arch to 
the 1889 World's Fair, is one of the most recognizable structures in the world. 
Standing 324 meters tall, it was the tallest man-made structure in the world for 41 years
until the completion of the Chrysler Building in New York City. 
The Eiffel Tower is named after the engineer Gustave Eiffel, whose company designed and built the tower. 
It is a global cultural icon of France and one of the most-visited paid monuments in the world, with 
millions of visitors every year."

"""


def get_gemini_response(prompt):
    model = genai.GenerativeModel('gemini-pro')
    try:
        response = model.generate_content([prompt])
        return response.text
    except Exception as e:
        print(f"Error generating response: {e}")
        return None

while(True):
    choice=int(input("\n1) Zero shot prompting\n2) Few shot prompting\n3)exit\nEnter your choice::"))
    if choice==1:

        print("=== Zero-Shot Prompting ===")
        zero_shot_prompt = zero_shot_template_string 
        response_zero_shot = get_gemini_response(zero_shot_prompt)
        if response_zero_shot:
            print(response_zero_shot)
        else:
            print("Failed to generate zero-shot response.")
    elif choice==2:
 
        print("\n=== Few-Shot Prompting ===")
        few_shot_prompt = few_shot_template_string 
        response_few_shot = get_gemini_response(few_shot_prompt)
        if response_few_shot:
            print(response_few_shot)
        else:
            print("Failed to generate few-shot response.")
    else:
        break