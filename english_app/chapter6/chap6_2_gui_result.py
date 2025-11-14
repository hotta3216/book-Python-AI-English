import FreeSimpleGUI as sg

# GUIの文字サイズを１４ポイントにする
sg.set_options(font=('Helvetica', 14))

def gui_result(number: int, result: str, japanese: str):
    """
    結果を表示し、
    ユーザーが確認できるようにする関数
    :param number: 問題番号
    :param result: 結果の文字列
    :param japanese: 結果の日本語訳付き文字列
    :return: ユーザーの選択 ('Next', 'Review', 'Cancel')
    """
    layout = [
        [sg.Multiline(default_text=result, disabled=True, background_color='white', text_color='black', size=(80, None), key='-RESULT-')],
        [sg.Button('次へ'), sg.Button('復習'), sg.Button('終了'), sg.Text('          '), sg.Button('翻訳')],
    ]
    window = sg.Window(f'Q{number} 結果', layout)

    while True:
        event, _ = window.read()
        if event == sg.WIN_CLOSED or event == '終了':
            window.close()
            return 'Cancel'
        elif event == '次へ':
            window.close()
            return 'Next'
        elif event == '復習':
            window.close()
            return 'Review'
        elif event == '翻訳':
            window['-RESULT-'].update(japanese)