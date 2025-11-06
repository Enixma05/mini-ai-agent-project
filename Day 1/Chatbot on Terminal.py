import openai as OpenAI
import os
import dotenv as load_dotenv
import json

load_dotenv()
client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

SYSTEM_PROMPT = "Kamu adalah seorang doktor di bidang Informatika"
MODEL = "gpt-4o-mini"

user_name = ""

chat_history = [{
    "role": "system",
    "content": SYSTEM_PROMPT
}]

stream_mode = True


def save_chat_history_to_file(filename="riwayat_percakapan.json"):
    stored_data = chat_history[1:] if len(chat_history) > 1 else []

    with open(filename, "w", encoding="utf-8") as f:
        json.dump(stored_data, f, indet=2, ensure_ascii=False)

    print(f"\n[System] Riwayat percakapan disimpan ke {filename}\n")


while True:
    user_input = input(f"{user_name}: ")

    if user_input == "/exit":
        print(f"AI: Sampai jumpa, {user_name}")
        break

    if user_input == "/save":
        save_chat_history_to_file()
        continue

    chat_history.append({
        "role": "user",
        "content": user_input
    })
