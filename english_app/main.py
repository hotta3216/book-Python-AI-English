import FreeSimpleGUI as sg

from chapter3.chap3_1_generate_questions import generate_questions
from chapter3.chap3_2_speak_text import speak_text
from chapter3.chap3_3_play_voice import play_voice
from chapter4.chap4_2_transcribe_audio import transcribe_audio
from chapter4.chap4_4_compare_text import compare_text
from chapter5.chap5_2_speak_and_record import speak_and_record
from chapter6.chap6_1_gui_start import gui_start
from chapter6.chap6_2_translate_en_to_ja import translate_en_to_ja
from chapter6.chap6_2_gui_result import gui_result
from chapter6.chap6_3_gui_final import gui_final

if __name__ == '__main__':
    initial_mode = True  # 条件入力時はTrue、同条件で再実行時はFalse

    while True: # 再実行ループ
        if initial_mode: # 同条件で再実行時は条件入力をスキップ
            # 条件入力
            cefr_level, speed, question_count, use_words = gui_start()

        # 問題と回答の生成
        qa_pairs = generate_questions(cefr_level, question_count, use_words)

        # 全体結果記録用リスト
        results = [['問題', '一致率 (%)']]

        # 問題数ループ
        for i, (q, a) in enumerate(qa_pairs, start=1):
            # 文字数をカウントし、録音時間を設定
            duration = max(5, len(a) // 10 + 2)  # 回答の長さに応じて録音時間を調整

            while True: # 同じ問題復習ループ
                if sg.popup_ok_cancel(f"Q{i} / {question_count}: スタート") == 'Cancel':
                    sg.popup("練習を中止しました")
                    exit()

                # 質問を2回読み上げ
                play_voice(speak_text(q))
                play_voice(speak_text(q))

                # 回答の読み上げと録音を同時に実行
                wav_path = speak_and_record(a, speed, duration)

                # ユーザーの回答を文字起こし
                text_result = transcribe_audio(wav_path)

                # 講師役の回答とユーザーの回答を比較
                result = compare_text(a, text_result)

                # 結果の文字列を生成
                result_str = (
                    f"【質問文】{q}\n"
                    f"【講師役の回答】 {a}\n"
                    f"【あなたの回答】 {text_result}\n"
                    f"【一致率】 {result['accuracy']}%\n"
                    f"【比較結果】 {result['highlight']}\n"
                    f"【間違えた単語】 {', '.join(result['diff_words'])}\n"
                    f"\n\n※ 質問文と回答文日本語訳は「翻訳」ボタンで表示できます。\n"
                )
                # 翻訳付きの結果文字列を生成
                result_str_japanese = (
                    f"{result_str}"  # 元の結果文字列
                    f"【質問の日本語訳】 {translate_en_to_ja(q)}\n"
                    f"【回答の日本語訳】 {translate_en_to_ja(a)}\n"
                )

                # 結果表示と次のアクション選択
                flag = gui_result(i, result_str, result_str_japanese)
                if flag == 'Cancel':
                    sg.popup("練習を中止しました")
                    exit() # アプリを終了
                elif flag == 'Review':
                    continue  # 同じ問題復習ループの先頭へ
                # flag == 'Next' の場合は結果をリストに追加したあとループを抜けて次の問題へ

                # 結果をリストに追加
                results.append([f'Q{i}', result["accuracy"]])

                break  # 同じ問題復習ループを抜けて次の問題へ

        # 全体の結果を表示
        flag = gui_final(cefr_level, results)

        if flag == None:
            sg.popup("練習を終了します。お疲れさまでした！", title='終了')
            break  # 再実行ループを抜けてアプリを終了
        elif flag == 'Continue':
            initial_mode = False  # 「同条件で再実行」選択時→条件入力をスキップ
        elif flag == 'Reset':
            initial_mode = True  # 「条件を再設定して再実行」選択時→条件入力を実行

        continue  # 再実行ループの先頭へ
