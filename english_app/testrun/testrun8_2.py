# 8.2節の動作確認用コード
from chapter3.chap3_1_generate_questions import generate_questions
from chapter3.chap3_2_speak_text import speak_text
from chapter3.chap3_3_play_voice import play_voice
from chapter8.chap8_2_determine_gender import determine_gender

if __name__ == "__main__":
    # 例: A1レベルで3つの質問と回答を生成
    word_list=['My name is John.', 'My name is Mira.', 'I am a teacher.']
    qa_pairs = generate_questions('A1', 3, use_words=word_list)

    for i, (q, a) in enumerate(qa_pairs, 1):
        # 問題文を音声化して再生
        print(f"Q{i}: {q}")
        q_audio = speak_text(q)
        play_voice(q_audio)

        # 回答文の話者の性別を判定し、音色を変更する
        gender = determine_gender(a)
        if gender == 'Male':
            voice = "Atlas-PlayAI"  # 男性の声
        elif gender == 'Female':
            voice="Gail-PlayAI"  # 女性の声
        else:
            voice = "Mamaw-PlayAI"  # 中性的な声

        # 回答文を音声化して再生
        print(f"A{i}: {a}")
        a_audio = speak_text(a, voice=voice)
        play_voice(a_audio)