# 4.4節の動作確認用コード
from chapter4.chap4_4_compare_text import compare_text

if __name__ == "__main__":
    correct = "Hello, world!"
    user = "Hello Python!"

    result = compare_text(correct, user)

    print("一致率:", result['accuracy'])
    print("ハイライト結果:", result['highlight'])
    print("間違えた単語:", result['diff_words'])