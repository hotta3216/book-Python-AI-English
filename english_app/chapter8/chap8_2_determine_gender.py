from dotenv import load_dotenv
from groq import Groq

load_dotenv()  # .envファイルからAPIキーを読み込む

# Groqの設定
client = Groq()
MODEL_CHAT = "llama-3.3-70b-versatile" # 文章生成用モデル

def determine_gender(text: str) -> str:
    """
    テキストから性別を判定する関数
    :param text: 入力テキスト
    :return: 性別判定結果 ('Male', 'Female', 'Neutral')
    """
    prompt = (
        "Determine whether the speaker of the following statement is male or female.\n"
        "Output 'Male' if male, 'Female' if female, or 'Neutral' if neither.\n"
        "Do NOT write explanations, only answer."
        f"Statement: {text}\n"
    )

    response = client.chat.completions.create(
        model=MODEL_CHAT,
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.3,
    )
    return response.choices[0].message.content.strip()