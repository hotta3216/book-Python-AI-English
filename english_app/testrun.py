# # 3.1節の動作確認用コード
# from chapter3.chap3_1_generate_questions import generate_questions

# if __name__ == "__main__":
#     qa_pairs = generate_questions('A1', 3, ['apple', 'orange'])
#     print("\nqa_pairs:\n", qa_pairs)


# # 3.2節の動作確認用コード
# from chapter3.chap3_2_speak_text import speak_text

# if __name__ == "__main__":
#     tmp_file_path = speak_text("Hello, this is a test of text to speech conversion.", speed=1.0)
#     print(f'{tmp_file_path} に音声データを保存しました')


# # 3.4節の動作確認用コード
# from chapter3.chap3_1_generate_questions import generate_questions
# from chapter3.chap3_2_speak_text import speak_text
# from chapter3.chap3_3_play_voice import play_voice

# if __name__ == "__main__":
#     # 例: A1レベルで3つの質問と回答を生成
#     qa_pairs = generate_questions('A1', 3)

#     for i, (q, a) in enumerate(qa_pairs, 1):
#         # 問題文を音声化して再生
#         print(f"Q{i}: {q}")
#         q_audio = speak_text(q)
#         play_voice(q_audio)

#         # 回答文を音声化して再生
#         print(f"A{i}: {a}")
#         a_audio = speak_text(a)
#         play_voice(a_audio)


# # 4.3節の動作確認用コード
# from chapter4.chap4_1_record_voice import record_voice
# from chapter4.chap4_2_transcribe_audio import transcribe_audio

# if __name__ == "__main__":
#     print("録音開始...")
#     tmp_file_path = record_voice(duration=5)  # 5秒録音
#     print("録音終了")
#     transcript = transcribe_audio(tmp_file_path)  # 録音した音声を文字起こし
#     print("文字起こし結果:", transcript)


# # 4.4節の動作確認用コード
# from chapter4.chap4_4_compare_text import compare_text

# if __name__ == "__main__":
#     correct = "Hello, world!"
#     user = "Hello Python!"

#     result = compare_text(correct, user)

#     print("一致率:", result['accuracy'])
#     print("ハイライト結果:", result['highlight'])
#     print("間違えた単語:", result['diff_words'])


# # 5.2節の動作確認用コード
# from chapter3.chap3_3_play_voice import play_voice
# from chapter5.chap5_2_speak_and_record import speak_and_record

# # 動作確認用
# if __name__ == '__main__':
#     answer = "My name is Bob."
#     print(f"Answer to speak: {answer}")
#     wav_path = speak_and_record(answer, speed=1.0, record_duration=5)
#     print(f"音声ファイル: {wav_path} を再生します")
#     play_voice(wav_path)


# # 6.1節の動作確認用コード
# from chapter6.chap6_1_gui_start import gui_start

# if __name__ == "__main__":
#     cefr_level, speed, question_count, use_words = gui_start()
#     print(f'CEFRレベル: {cefr_level}\n読み上げ速度: {speed}\n生成する問題数: {question_count}\n使用する単語: {use_words}')


# # 6.2節の動作確認用コード
# from chapter6.chap6_2_translate_en_to_ja import translate_en_to_ja
# from chapter6.chap6_2_gui_result import gui_result

# # 動作確認用
# if __name__ == "__main__":
#     result_english = "This is a sample result."
#     result_japanese = translate_en_to_ja(result_english)
#     result = gui_result(1, result_english, result_japanese)
#     print(f'User selected: {result}')


# # 6.3節の動作確認用コード
# from chapter6.chap6_3_gui_final import gui_final

# if __name__ == "__main__":
#     sample_results = [
#         ['問題', '一致率(%)'],
#         [1, 76.2],
#         [2, 77.8],
#         [3, 91.4],
#         [4, 76.5],
#         [5, 86.8],
#     ]
#     user_choice = gui_final('A2', sample_results)
#     print(f'User selected: {user_choice}')


# # 8.2節の動作確認用コード
# from chapter3.chap3_1_generate_questions import generate_questions
# from chapter3.chap3_2_speak_text import speak_text
# from chapter3.chap3_3_play_voice import play_voice
# from chapter8.chap8_2_determine_gender import determine_gender

# if __name__ == "__main__":
#     # 例: A1レベルで3つの質問と回答を生成
#     word_list=['My name is John.', 'My name is Mira.', 'I am a teacher.']
#     qa_pairs = generate_questions('A1', 3, use_words=word_list)

#     for i, (q, a) in enumerate(qa_pairs, 1):
#         # 問題文を音声化して再生
#         print(f"Q{i}: {q}")
#         q_audio = speak_text(q)
#         play_voice(q_audio)

#         # 回答文の話者の性別を判定し、音色を変更する
#         gender = determine_gender(a)
#         if gender == 'Male':
#             voice = "Atlas-PlayAI"  # 男性の声
#         elif gender == 'Female':
#             voice="Gail-PlayAI"  # 女性の声
#         else:
#             voice = "Mamaw-PlayAI"  # 中性的な声

#         # 回答文を音声化して再生
#         print(f"A{i}: {a}")
#         a_audio = speak_text(a, voice=voice)
#         play_voice(a_audio)
