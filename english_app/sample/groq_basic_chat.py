from dotenv import load_dotenv
from groq import Groq

load_dotenv()  # .envファイルからAPIキーを読み込む

client = Groq()

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "プログラミング言語Pythonについて、100文字以内で説明してください。",
        }
    ],
    model="llama-3.3-70b-versatile"
)

print(chat_completion.choices[0].message.content)
