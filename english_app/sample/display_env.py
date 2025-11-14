import os
from dotenv import load_dotenv

# .env ファイルを読み込む
load_dotenv()

# 環境変数を取得して表示
print(os.getenv("GROQ_API_KEY"))