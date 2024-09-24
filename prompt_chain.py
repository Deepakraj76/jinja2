from jinja2 import Template
import google.generativeai as genai

# Load environment variables
genai.configure(api_key="AIzaSyC-onsUqc_veajLrXKnr5g3iUJiduyTnQg")

# Template for extracting quotes and answering questions in one prompt
prompt_template = """
You are given a large document and a specific question. 
First, extract the most relevant quotes from the document that directly help answer the question. 
Then, based on these quotes and the overall context of the document, provide a detailed answer to the question.

Document: {{ document }}

Question: {{ question }}

Output: 
1. A list of the most relevant quotes from the document.
2. A detailed answer to the question using the extracted quotes and overall context.
"""

# Example document and question
document = """
Climate change is one of the most pressing issues in the 21st century. 
It is primarily driven by human activities, particularly the burning of fossil fuels, 
which increases the concentration of greenhouse gases in the atmosphere. 
These gases trap heat and lead to global warming. As a result, we have observed more 
extreme weather events, rising sea levels, and changes in ecosystems. Governments and 
organizations worldwide are working on policies to reduce emissions and transition to renewable energy.
"""

question = "What is causing climate change?"

# Function to generate the prompt from the template
def generate_combined_prompt(document, question):
    template = Template(prompt_template)
    return template.render(document=document, question=question)

# Function to get a response from Google Gemini API
def get_gemini_response(prompt):
    model = genai.GenerativeModel('gemini-pro')
    try:
        response = model.generate_content([prompt])
        return response.text
    except Exception as e:
        print(f"Error generating response: {e}")
        return None

while True:
    choice = int(input("\n1) Combined Prompt\n2) Exit\nEnter your choice:  "))
    if choice == 1:
        print("=== Combined Prompt ===")
        # Generate prompt using the document and question
        combined_prompt = generate_combined_prompt(document, question)
        response = get_gemini_response(combined_prompt)
        
        if response:
            print(response)
        else:
            print("Failed to generate response.")
    else:
        break
