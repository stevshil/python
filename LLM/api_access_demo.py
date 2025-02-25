import openai

from openai import OpenAI
import os

# openai.api_key = getpass.getpass("Enter your OpenAI API key: ")
openai.api_key = os.environ.get("OPENAI_API_KEY")

client = OpenAI(api_key = openai.api_key)

def some_fun():
    completion = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "What is human life expectancy in the United States?"},
        {"role": "system", "content": "Human life expectancy in the United States is 78 years."},
        {"role": "user", "content": "What is the square root of banana?"}
    ]
    )

    # print(completion)
    print(completion.choices[0].message.content)

    completion = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role": "system", "content": "You are a lying grumpy old man."},
        {"role": "user", "content": "What is human life expectancy in the United States?"},
        {"role": "system", "content": "Human life expectancy in the United States is 78 years."},
        {"role": "user", "content": "What is the distance from the sun to the moon?"}
    ]
    )

    print(completion.choices[0].message.content)

def get_response(question):
    completion = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": question}
        ]
    )
    return completion.choices[0].message.content


def role_response(question, role):
    completion = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": role},
            {"role": "user", "content": question}
        ]
    )
    return completion.choices[0].message.content


# some_fun
print(get_response("What is the capital of Italy?"))
print(get_response("What is the capital of France?"))

# What about context across questions?

italy = get_response("What is the capital of Italy?")
print(get_response(f"What is the population of {italy}?"))

print(role_response("Tell me a story about an evil rooster.","You are a talented author who has one many awards for your writing."))