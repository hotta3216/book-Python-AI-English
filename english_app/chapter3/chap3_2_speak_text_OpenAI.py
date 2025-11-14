import tempfile
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()  # .envファイルからAPIキーを読み込む

# OpenAIの設定
client = OpenAI()
MODEL_TTS = "gpt-4o-mini-tts"  # TTSモデル
DEFAULT_VOICE = "alloy"  # TTSの声の種類のデフォルト

def speak_text(text: str, speed: float = 1.0, voice: str = DEFAULT_VOICE) -> str:
    """
    指定したテキストをTTSで読み上げた音声を一時ファイルに保存する関数
    :param text: 読み上げる文章
    :param speed: 読み上げ速度（1.0=標準, 0.5=遅い, 2.0=速い など）
    :param voice: 声の種類
    """
    # 音声データ取得
    response = client.audio.speech.create(
        model=MODEL_TTS,
        voice=voice,
        input=text,
        response_format="wav",
        speed=speed
    )
    # 一時ファイルに保存
    with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmp_file:
        response.write_to_file(tmp_file.name)

    # 一時ファイルのパスを返す
    return tmp_file.name

# 動作確認
if __name__ == "__main__":
    tmp_file_path = speak_text("Hello, this is a test of text to speech conversion.", speed=1.0)
    print(f'{tmp_file_path} に音声データを保存しました')
