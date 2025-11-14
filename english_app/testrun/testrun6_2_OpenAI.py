# 6.2節の動作確認用コード
from chapter6.chap6_2_translate_en_to_ja_OpenAI import translate_en_to_ja
from chapter6.chap6_2_gui_result import gui_result

# 動作確認用
if __name__ == "__main__":
    result_english = "This is a sample result."
    result_japanese = translate_en_to_ja(result_english)
    result = gui_result(1, result_english, result_japanese)
    print(f'User selected: {result}')