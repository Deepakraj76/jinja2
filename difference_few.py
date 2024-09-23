from jinja2 import Template
import google.generativeai as genai

# Load environment variables
genai.configure(api_key="AIzaSyC-onsUqc_veajLrXKnr5g3iUJiduyTnQg")  # Set this in your environment



# Few-Shot Prompting Template (With examples)
few_shot_template_string = """
Here are some examples of calculating expressions:

Example 1: 
Calculate 6 + 2 * (3 - 1):
Answer: 6 + 2 * 2 = 6 + 4 = 10.

Example 2: 
Calculate (8 / 4) + 3 * 5:
Answer: 2 + 3 * 5 = 2 + 15 = 17.

Now, calculate the expression: 5 + (3 * 2) - 4 / 2.
"""

# Function to generate content using a Gemini model
def get_gemini_response(prompt):
    model = genai.GenerativeModel('gemini-pro')
    try:
        response = model.generate_content([prompt])
        return response.text
    except Exception as e:
        print(f"Error generating response: {e}")
        return None



# Generate Few-Shot response
print("\n=== Few-Shot Prompting ===")
few_shot_prompt = few_shot_template_string  # Task with examples
response_few_shot = get_gemini_response(few_shot_prompt)
if response_few_shot:
    print(response_few_shot)
else:
    print("Failed to generate few-shot response.")
