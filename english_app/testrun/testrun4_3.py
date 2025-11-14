# 4.3節の動作確認用コード
from chapter4.chap4_1_record_voice import record_voice
from chapter4.chap4_2_transcribe_audio import transcribe_audio

if __name__ == "__main__":
    print("録音開始...")
    tmp_file_path = record_voice(duration=5)  # 5秒録音
    print("録音終了")
    transcript = transcribe_audio(tmp_file_path)  # 録音した音声を文字起こし
    print("文字起こし結果:", transcript)