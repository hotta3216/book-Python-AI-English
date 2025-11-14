import difflib
import re

def compare_text(correct_text: str, user_text: str):
    """
    正解文とユーザー発話（文字起こし）を比較し、
    一致率と間違えた単語のハイライト結果を返す関数。
    :param correct_text: 正解の文章
    :param user_text: ユーザーの文字起こし文章
    :return: 比較結果をまとめた辞書
    """
    # 単語を小文字化して英数字と空白以外を除去し、単語リストに分割
    def tokenize(text):
        text = text.lower() # すべて小文字化
        text = re.sub(r"[^\w\s]", "", text)  # 英数字と空白以外を除去
        return text.split() # 単語に分割したリストを返す

    correct_words = tokenize(correct_text)
    user_words = tokenize(user_text)

    # 一致率計算
    matcher = difflib.SequenceMatcher(None, correct_words, user_words)
    accuracy = matcher.ratio() * 100

    # 差分取得
    diff = list(difflib.ndiff(correct_words, user_words))

    # 間違えた単語とハイライト作成
    diff_words = []
    highlight_result = []

    for token in diff:
        if token.startswith("  "):  # 一致
            highlight_result.append(token[2:])
        elif token.startswith("- "):  # 正解文にあるがユーザーが欠落
            highlight_result.append(f"[{token[2:]}❌]")
            diff_words.append(token[2:])
        elif token.startswith("+ "):  # ユーザーが余計に発音
            highlight_result.append(f"[+{token[2:]}]")
            diff_words.append(token[2:])

    return {
        "accuracy": round(accuracy, 1),
        "highlight": " ".join(highlight_result),
        "diff_words": diff_words
    }