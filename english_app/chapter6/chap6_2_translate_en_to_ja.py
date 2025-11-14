from dotenv import load_dotenv
from groq import Groq

load_dotenv()  # .envファイルからAPIキーを読み込む

# Groqの設定
client = Groq()
MODEL_CHAT = "llama-3.3-70b-versatile" # 英文生成用モデル

def translate_en_to_ja(english_text: str) -> str:
    """
    英文を日本語に翻訳する関数
    :param english_text: 英文
    :return: 日本語訳
    """
    prompt = (
        "次の英文を自然でわかりやすい日本語に直してください。"
        f"{english_text}\n"
    )

    response = client.chat.completions.create(
        model=MODEL_CHAT,
        messages=[
            {"role": "system", "content": "あなたはプロの翻訳家です。"},
            {"role": "user", "content": prompt}
        ],
        temperature=0.3,
    )
    japanese_text = response.choices[0].message.content.strip()
    return japanese_text
