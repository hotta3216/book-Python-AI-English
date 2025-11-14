# 3.2節の動作確認用コード
from chapter3.chap3_2_speak_text_OpenAI import speak_text

if __name__ == "__main__":
    tmp_file_path = speak_text("Hello, this is a test of text to speech conversion.", speed=1.0)
    print(f'{tmp_file_path} に音声データを保存しました')