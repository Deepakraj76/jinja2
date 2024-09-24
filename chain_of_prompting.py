from jinja2 import Template
import google.generativeai as genai

# Load environment variables
genai.configure(api_key="AIzaSyC-onsUqc_veajLrXKnr5g3iUJiduyTnQg")

few_shot_prompt="""
The odd numbers in this group add up to an even number: 4, 8, 9, 15, 12, 2, 1.
A: The answer is False.
The odd numbers in this group add up to an even number: 17,  10, 19, 4, 8, 12, 24.
A: The answer is True.
The odd numbers in this group add up to an even number: 16,  11, 14, 4, 8, 13, 24.
A: The answer is True.
The odd numbers in this group add up to an even number: 17,  9, 10, 12, 13, 4, 2.
A: The answer is False.
The odd numbers in this group add up to an even number: 15, 32, 5, 13, 82, 7, 1. 
A: 

"""

# chain of prompting
chain_of_prompt="""
The odd numbers in this group add up to an even number: 4, 8, 9, 15, 12, 2, 1.
A: Adding all the odd numbers (9, 15, 1) gives 25. The answer is False.

The odd numbers in this group add up to an even number: 17,  10, 19, 4, 8, 12, 24.
A: Adding all the odd numbers (17, 19) gives 36. The answer is True.

The odd numbers in this group add up to an even number: 16,  11, 14, 4, 8, 13, 24.
A: Adding all the odd numbers (11, 13) gives 24. The answer is True.

The odd numbers in this group add up to an even number: 17,  9, 10, 12, 13, 4, 2.
A: Adding all the odd numbers (17, 9, 13) gives 39. The answer is False.

now,
The odd numbers in this group add up to an even number: 15, 32, 5, 13, 82, 7, 1. 

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
    choice=int(input("\n1) few_shot_prompting\n2) chain_of _prompting\n3) Exit\nEnter your choice:  "))
    if choice==2:

        print("=== chain_of_prompting ===")
        prompt = chain_of_prompt
        response = get_gemini_response(prompt)
        if response:
            print(response)
        else:
            print("Failed to generate  response.")
    elif choice==1:

        print("=== few_shot_prompting ===")
        prompt = few_shot_prompt
        response = get_gemini_response(prompt)
        if response:
            print(response)
        else:
            print("Failed to generate  response.")
    
    else:
        break