# 5.2節の動作確認用コード
from chapter3.chap3_3_play_voice import play_voice
from chapter5.chap5_2_speak_and_record import speak_and_record

# 動作確認用
if __name__ == '__main__':
    answer = "My name is Bob."
    print(f"Answer to speak: {answer}")
    wav_path = speak_and_record(answer, speed=1.0, record_duration=5)
    print(f"音声ファイル: {wav_path} を再生します")
    play_voice(wav_path)