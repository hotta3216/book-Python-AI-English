import FreeSimpleGUI as sg

# GUIの文字サイズを１４ポイントにする
sg.set_options(font=('Helvetica', 14))

def gui_final(cefr_level: str, results: list):
    """
    結果を表示し、
    ユーザーが確認できるようにする関数
    :param cefr_level: CEFRレベル
    :param results: 問題と一致率のリスト
    :return: ユーザーの選択 ('Continue', 'Reset', None)
    """
    layout = [
        [sg.Text(f'CEFR_Level : {cefr_level}', background_color='white', text_color='black')],
        [sg.Table(values=results[1:], headings=results[0], col_widths=(5, 10), auto_size_columns=False, justification='center', num_rows=min(20, len(results)-1))],
        [sg.Button('終了'), sg.Button('同条件で再実行'), sg.Button('条件を再設定して再実行')],
    ]
    window = sg.Window('総合結果', layout)

    while True:
        event, _ = window.read()
        if event == sg.WIN_CLOSED or event == '終了':
            window.close()
            return None
        elif event == '同条件で再実行':
            window.close()
            return 'Continue'
        elif event == '条件を再設定して再実行':
            window.close()
            return 'Reset'