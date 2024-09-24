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

# Create a list of iterations for the slogans
iterations = range(3)  # Modify the number of slogans you want to generate

# Prepare the Jinja2 template for the prompt, with a for loop
template_string = """
{% for i in iterations %}
Slogan {{ i + 1 }}:
Create a catchy marketing slogan for a product called '{{ product_name }}', which is an {{ product_type }}. 
The key benefits are: {{ key_benefits }}. 
The slogan should be engaging, memorable, and convey the eco-friendly nature of the product.

{% endfor %}
"""

# Create the Jinja2 template
template = Template(template_string)

# Render the template with the product details and iterations
prompt = template.render(
    product_name=product_name,
    product_type=product_type,
    key_benefits=', '.join(key_benefits),
    iterations=iterations
)

# Load environment variables
genai.configure(api_key="AIzaSyC-onsUqc_veajLrXKnr5g3iUJiduyTnQg")  # Make sure to set this in your environment

def get_gemini_response(prompt):
    model = genai.GenerativeModel('gemini-pro')
    try:
        response = model.generate_content([prompt])
        return response.text
    except Exception as e:
        print(f"Error generating response: {e}")
        return None

# Generate the response using the prompt containing multiple slogans
response = get_gemini_response(prompt)

if response:
    print(response)
else:
    print("Failed to generate a response.")
