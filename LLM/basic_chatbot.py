import openai

from openai import OpenAI
import os

# Set your OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")
messages=[]

# def chatbot(prompt,last_context):
def chatbot(prompt):
    client = OpenAI(api_key = openai.api_key)
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            *prompt  # Flatten the array to a comma-separated list of dictionary values
        ],
        max_tokens=150
    )
    return response.choices[0].message.content

if __name__ == "__main__":
    print("Welcome to the chatbot! Type 'exit' to end the conversation.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            break
        messages.append({"role": "user", "content": user_input})
        response = chatbot(messages)
        print("Bot:", response)