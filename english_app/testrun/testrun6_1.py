# 6.1節の動作確認用コード
from chapter6.chap6_1_gui_start import gui_start

if __name__ == "__main__":
    cefr_level, speed, question_count, use_words = gui_start()
    print(f'CEFRレベル: {cefr_level}\n読み上げ速度: {speed}\n生成する問題数: {question_count}\n使用する単語: {use_words}')