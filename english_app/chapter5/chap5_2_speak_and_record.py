from concurrent.futures import ThreadPoolExecutor

from chapter3.chap3_2_speak_text import speak_text
from chapter3.chap3_3_play_voice import play_voice
from chapter4.chap4_1_record_voice import record_voice

def speak_and_record(answer_text: str, speed: float, record_duration: int = 5) -> str:
    """
    回答を読み上げ、同時にユーザーの回答を録音する関数
    :param answer_text: 読み上げる回答文
    :param record_duration: 録音時間（秒）
    :return: 録音結果の一時ファイルパス
    """

    # 音声合成を行い、一時ファイルに保存
    voice_file = speak_text(answer_text, speed=speed)

    with ThreadPoolExecutor() as executor:
        # 録音を別スレッドで開始
        future_record = executor.submit(record_voice, record_duration)

        # 同時に読み上げ
        play_voice(voice_file)

        # 録音終了後に結果取得
        recorded_file = future_record.result()
        return recorded_file