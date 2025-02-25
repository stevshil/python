import torch
import os
from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline, AutoModelForSequenceClassification

# Environment setup
os.environ['TOKENIZERS_PARALLELISM'] = 'false'
torch.manual_seed(42)

# Business text for analysis
business_text = "TechCorp's Q3 revenue increased by 15.7%, reaching $42.5M. CEO Jane Smith attributes this growth to the successful launch of AI-powered products."

print("Business text:")
print(business_text)
print("\nYour task: Tokenize this text and analyze the results.")

# Load pre-trained model and tokenizer
tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")
model = AutoModelForSequenceClassification.from_pretrained("bert-base-uncased")

# Sample text
text = business_text

# Tokenize the text
inputs = tokenizer(text, return_tensors="pt")

# Analyze the results
with torch.no_grad():
    outputs = model(**inputs)

print("Tokens:", tokenizer.convert_ids_to_tokens(inputs["input_ids"].squeeze().tolist()))
print("Token Scores:", outputs.logits)