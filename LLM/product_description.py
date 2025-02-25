### YOUR CODE HRE
from transformers import pipeline

def generate_product_description(product_prompt, max_len=100):
    """
    Generate a product description based on a prompt.
    
    Args:
        product_prompt (str): A brief description of the product
        max_length (int): Maximum length of the generated text
        
    Returns:
        str: Generated product description
    """
    # YOUR CODE HERE
    # Load a pre-trained language model
    generator = pipeline('text-generation', model='distilgpt2')
    # Generate the product description
    product_description = generator(product_prompt, max_length=max_len, num_return_sequences=1, truncation=True)
    
    
    return product_description[0]['generated_text']

# Test prompts
business_prompts = [
    "TechCorp's new AI-powered customer analytics platform helps businesses",
    "Introducing CloudSync, a secure file-sharing solution for enterprises that",
    "TechVision AR glasses are designed for professionals who need"
]

generate_product_description(business_prompts[0],150)