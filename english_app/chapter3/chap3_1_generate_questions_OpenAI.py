import re
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()  # .envファイルからAPIキーを読み込む

# OpenAIの設定
client = OpenAI()
MODEL_CHAT = "gpt-4o-mini"  # 英文生成用モデル

def generate_questions(cefr_level: str, question_count: int, use_words: list = None) -> list:
    """
    AIのAPIを使って、カランメソッド形式の質問と回答を生成する関数
    :param cefr_level: 'A1', 'A2', 'B1', ...
    :param question_count: 生成するQ&Aの数
    :param use_words: 使用する単語リスト（オプション）
    :return: [[質問1, 回答1], [質問2, 回答2], ...] の2次元リスト
    """

    if question_count == 1:
        # 質問文が1つだけのときのプロンプト
        questions = f'one question and answer'
    else:
        # 質問文が複数あるときのプロンプト
        questions = f'{question_count} questions and answers'
    
    if use_words:
        words_str = ', '.join(use_words)
        prompt_words = f"Use the following words in the answers: {words_str}."
    else:
        prompt_words = "Use common vocabulary appropriate for the CEFR level."

    prompt = (
        "You are an English teacher using the Callan Method.\n"
        f"Generate {questions} for speaking practice.\n"
        "Requirements:\n"
        f"- CEFR Level: {cefr_level}\n"
        "- Each answer should be a complete sentence.\n"
        "- Do NOT write explanations, only Q&A.\n"
        "- Use American English.\n"
        f"- {prompt_words}\n"
        "- Format:\n"
        "Q1: ...\n"
        "A1: ..."
    )

    response = client.chat.completions.create(
        model=MODEL_CHAT,
        messages=[
            {"role": "system", "content": "You are a helpful English teacher."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7,
    )
    qa_text = response.choices[0].message.content.strip()
    # print("\nqa_text:\n", qa_text) # デバッグ用

    # 正規表現でQ&Aを抽出
    pattern = r"Q\d+:\s*(.+?)\s*A\d+:\s*(.+?)(?=(?:Q\d+:)|$)"
    matches = re.findall(pattern, qa_text, re.DOTALL)
    # print("\nmatches:\n", matches) # デバッグ用

    # 改行や余計な空白を整形
    qa_pairs = [[q.strip(), a.strip()] for q, a in matches]

    return qa_pairs