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
        'example_benefits': "100% biodegradable, safe for children and pets"
    },
    {
        'example_slogan': "EcoClean - Tough on stains, gentle on nature.",
        'example_benefits': "Powerful stain removal, eco-friendly packaging"
    }
]

# Create a list of iterations for the slogans
iterations = range(3)  # Number of slogans you want to generate

# Prepare the Jinja2 template with few-shot examples and a for loop
template_string = """
Here are a few examples of catchy marketing slogans for products similar to '{{ product_name }}' which is an {{ product_type }}:

{% for example in few_shot_examples %}
Example {{ loop.index }}:
Slogan: "{{ example.example_slogan }}"
Key Benefits: {{ example.example_benefits }}

{% endfor %}

Now, please create {{ iterations | length }} catchy marketing slogans for '{{ product_name }}'. The key benefits are: {{ key_benefits }}. 
The slogans should be engaging, memorable, and convey the eco-friendly nature of the product.

{% for i in iterations %}
Slogan {{ i + 1 }}:

{% endfor %}
"""

# Create the Jinja2 template
template = Template(template_string)

# Render the template with product details, few-shot examples, and iterations
prompt = template.render(
    product_name=product_name,
    product_type=product_type,
    key_benefits=', '.join(key_benefits),
    few_shot_examples=few_shot_examples,
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

# Generate the response using the prepared prompt with few-shot examples
response = get_gemini_response(prompt)

if response:
    print(response)
else:
    print("Failed to generate a response.")
