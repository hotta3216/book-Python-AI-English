import os

import sounddevice as sd
import soundfile as sf

def play_voice(voice_file: str):
    """ 音声ファイルを再生する関数
    :param tmp_file: 一時ファイルのパス
    """
    data, samplerate = sf.read(voice_file) # soundfileで読み込み
    sd.play(data, samplerate) # sounddeviceで再生
    sd.wait() # 再生終了まで待機

    # 一時ファイルを削除
    os.remove(voice_file)