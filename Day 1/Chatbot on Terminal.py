from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

SYSTEM_PROMPT = "Kamu adalah seorang doktor di bidang Informatika"

history = [
    {"role": "system", "content": SYSTEM_PROMPT}
]

while True:
    user_input = input("Kamu: ")

    if user_input == "/exit":
        break

    history.append({"role": "user", "content": user_input})

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=history
    )

    history.append({
        "role": "assistant",
        "content": response.choices[0].message.content
    })

    print(f"AI: {response.choices[0].message.content}")
