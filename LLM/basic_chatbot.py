import openai

from openai import OpenAI
import os

# Set your OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

def chatbot(prompt,last_context):
    client = OpenAI(api_key = openai.api_key)
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt+" "+last_context}
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
        try:
            lastresponse=response
        except:
            lastresponse=""
        # print("Last response: ", lastresponse)
        response = chatbot(user_input,lastresponse)
        print("Bot:", response)