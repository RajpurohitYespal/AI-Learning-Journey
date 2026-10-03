import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

my_api_key = os.getenv("GROQ_API_KEY")

if not my_api_key:
    raise ValueError("API key kaha hai bhai")

client = Groq(api_key=my_api_key)

model = "openai/gpt-oss-20b"

role = "user"

prompt = "I Love You"

message_system={
    "role":"system",
    "content":"you are my strict offfice collegue and my manager"
}

message = {
    "role": role,
    "content": prompt
}

messages = [message_system,message]

response = client.chat.completions.create(
    model=model,
    messages=messages,
    temperature=2
)

# print(response)

print("#######################################")

answer = response.choices[0].message.content

print(answer)