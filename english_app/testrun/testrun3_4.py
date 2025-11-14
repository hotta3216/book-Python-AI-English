# 3.4節の動作確認用コード
from chapter3.chap3_1_generate_questions import generate_questions
from chapter3.chap3_2_speak_text import speak_text
from chapter3.chap3_3_play_voice import play_voice

if __name__ == "__main__":
    # 例: A1レベルで3つの質問と回答を生成
    qa_pairs = generate_questions('A1', 3)

    for i, (q, a) in enumerate(qa_pairs, 1):
        # 問題文を音声化して再生
        print(f"Q{i}: {q}")
        q_audio = speak_text(q)
        play_voice(q_audio)

        # 回答文を音声化して再生
        print(f"A{i}: {a}")
        a_audio = speak_text(a)
        play_voice(a_audio)