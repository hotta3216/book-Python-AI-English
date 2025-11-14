import os

from dotenv import load_dotenv
from groq import Groq

load_dotenv()  # .envファイルからAPIキーを読み込む

# Groqの設定
client = Groq()
MODEL_TRANSCRIPTION = "whisper-large-v3-turbo" # 文字起こしモデル

def transcribe_audio(file_path: str) -> str:
    """
    一時ファイルの音声を文字起こし（Whisper API使用）
    :param file_path: WAVなどの音声ファイルパス
    :return: 文字起こし結果の文字列
    """
    prompt='The following is spoken in American English. Transcribe it accurately in English only. ' + \
            'Always spell out numbers instead of using digits (e.g., "20" → "twenty").'

    with open(file_path, "rb") as audio_file: # 音声ファイルをオープン
        transcript = client.audio.transcriptions.create( # 文字起こしAPI呼び出し
            model=MODEL_TRANSCRIPTION, # モデル指定
            file=audio_file, # 音声ファイル
            language="en",  # 英語設定
            prompt=prompt, # プロンプト指定
        )

    os.remove(file_path)  # 一時ファイルを削除

    return transcript.text.strip()