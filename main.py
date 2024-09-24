from jinja2 import Template
import os
import google.generativeai as genai

template_string = """
You are an assistant tasked with writing an email. Please generate an email with the following details:

Recipient: {{ recipient }}
Subject: {{ subject }}
Content: 
{% if tone == 'formal' %}
Dear {{ customer_name }},

We regret to inform you that the product "{{ product }}" is no longer available. However, we believe you might be interested in a similar product called "{{ similar_product }}". Please let us know if you would like more information about this alternative.

Thank you for your understanding.

Sincerely,
{{ sender }}

{% elif tone == 'friendly' %}
Hi {{ customer_name }},

I hope you're doing well! I wanted to let you know that the product "{{ product }}" is no longer available. However, I think you might like a similar product called "{{ similar_product }}". Let me know if you’d like more info!

Cheers,
{{ sender }}

{% elif tone == 'professional' %}
Hello {{ customer_name }},

I wanted to inform you that the product "{{ product }}" is no longer available. However, you might be interested in a similar product called "{{ similar_product }}". Please reach out if you would like more details.

Best regards,
{{ sender }}
{% endif %}
Tone: {{ tone }}
"""

# Define your variables
recipient = "customer@example.com"
subject = "Product Availability Update"
sender = "Jane Smith"
tone = "formal"
customer_name="John Doe",
product="Product A",
similar_product="Product B",

# Prepare the email content
template = Template(template_string)
email_content = template.render(
    recipient=recipient,
    subject=subject,
    customer_name=customer_name,
    product=product,
    similar_product=similar_product,
    sender=sender,
    tone=tone
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

response1 = get_gemini_response(email_content)

if response1:
    print(response1)
else:
    print("Failed to generate a response.")
