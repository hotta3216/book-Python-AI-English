import tempfile
import wave
import numpy as np
import sounddevice as sd

def record_voice(duration=5, samplerate=44100):
    """
    マイクから音声を録音し、一時ファイル(WAV)として保存
    :param duration: 録音時間（秒）
    :param samplerate: サンプリングレート（Hz）
    :return: 一時ファイルのパス
    """
    audio_data = sd.rec(int(duration * samplerate), samplerate=samplerate, channels=1, dtype=np.int16)
    sd.wait()

    # 一時ファイル作成とWAV保存をまとめてwith文で処理
    with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmp_file: # 一時ファイルを作成
        tmp_file_path = tmp_file.name # 一時ファイルのパスを取得
        with wave.open(tmp_file_path, 'wb') as wf: # WAVファイルとして保存
            wf.setnchannels(1)  # モノラル
            wf.setsampwidth(2)  # 16bit
            wf.setframerate(samplerate) # サンプリングレート
            wf.writeframes(audio_data.tobytes()) # 録音データを書き込み

    return tmp_file_path # 一時ファイルのパスを返す