# 6.3節の動作確認用コード
from chapter6.chap6_3_gui_final import gui_final

if __name__ == "__main__":
    sample_results = [
        ['問題', '一致率(%)'],
        [1, 76.2],
        [2, 77.8],
        [3, 91.4],
        [4, 76.5],
        [5, 86.8],
    ]
    user_choice = gui_final('A2', sample_results)
    print(f'User selected: {user_choice}')