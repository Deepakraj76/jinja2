from jinja2 import Template
import google.generativeai as genai

# Define the product details
product_name = "EcoClean"
product_type = "cleaning solution"
key_benefits = [
    "100% biodegradable",
    "safe for children and pets",
    "powerful stain removal",
    "eco-friendly packaging"
]

# Few-shot examples for better understanding of the task
few_shot_examples = [
    {
        'example_slogan': "EcoClean - Clean your home, save the planet!",
        'key_benefits': '[100% biodegradable,eco-friendly packaging]'
    },
    {
        'example_slogan': "EcoClean - Tough on stains, gentle on nature.",
        'key_benefits': '[100% biodegradable,powerful stain removal]'
    }
]

# Create a list of iterations for the slogans
iterations = range(3)  

# Prepare the Jinja2 template with few-shot examples and a for loop
template_string = """
Here are a few examples of catchy marketing slogans for products similar to '{{ product_name }}'
which is an {{ product_type }}:

{% for example in few_shot_examples %}
Example {{ loop.index }}:
Slogan: "{{ example.example_slogan }}"
Key_words: "{{example.key_benefits}}"
{% endfor %}

Now, please create {{ iterations | length }} catchy marketing slogans for '{{ product_name }}'.
The key benefits are: {{ key_benefits }}. 
The slogans should be engaging, memorable, and convey the eco-friendly nature of the product.

"""

template = Template(template_string)


prompt = template.render(
    product_name=product_name,
    product_type=product_type,
    key_benefits=', '.join(key_benefits),
    few_shot_examples=few_shot_examples,
    iterations=iterations
)

print(prompt)

# # Load environment variables
# genai.configure(api_key="AIzaSyC-onsUqc_veajLrXKnr5g3iUJiduyTnQg")  
# def get_gemini_response(prompt):
#     model = genai.GenerativeModel('gemini-pro')
#     try:
#         response = model.generate_content([prompt])
#         return response.text
#     except Exception as e:
#         print(f"Error generating response: {e}")
#         return None


# response = get_gemini_response(prompt)

# if response:
#     print(response)
# else:
#     print("Failed to generate a response.")
