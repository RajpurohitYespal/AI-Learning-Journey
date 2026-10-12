
import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

my_api_key = os.getenv("GROQ_API_KEY")

if not my_api_key:
    raise ValueError("API key kaha hai bhai")

client = Groq(api_key=my_api_key)

model = "openai/gpt-oss-20b"

knowledge_base = {
    "age": "Age of Prathyush is 21",
    "net worth": "Net worth of Prathyush is 2000"
}


def retrieve(question):
    question = question.lower()

    if "age" in question or "old" in question:
        return knowledge_base["age"]
    elif "net worth" in question:
        return knowledge_base["net worth"]
    else:
        return None


def ask_llm(question):
    context = retrieve(question)

    sys_prompt = f"""Answer in 1 line.
Answer only based on this context.
Do not hallucinate.
Context: {context}"""

    system_message = {
        "role": "system",
        "content": sys_prompt
    }

    message = {
        "role": "user",
        "content": question
    }

    messages = [system_message, message]

    response = client.chat.completions.create(
        model=model,
        messages=messages
    )

    answer = response.choices[0].message.content
    return answer


question = "How old is Prathyush?"

answer = ask_llm(question)
print(answer)
