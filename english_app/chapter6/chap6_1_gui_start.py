import FreeSimpleGUI as sg

# GUIの文字サイズを１４ポイントにする
sg.set_options(font=('Helvetica', 14))

# 条件入力用GUI
def gui_start():
    """
    ユーザーにCEFRレベル、読み上げ速度、生成する問題数を入力させるGUI
    :return: (cefr_level, speed, question_count, use_words) タプル
    """
    layout = [
        [sg.Text('CEFRレベルを選択してください:')],
        [sg.Listbox(values=['C2', 'C1', 'B2', 'B1', 'A2', 'A1'], default_values='A1', size=(20, 6), key='-CEFR-')],
        [sg.Text('読み上げ速度を選択してください:')],
        [sg.Slider(range=(0.5, 2.0), resolution=0.1, default_value=0.8, orientation='h', key='-SPEED-')],
        [sg.Text('生成する問題数を入力してください:')],
        [sg.Spin(values=list(range(1, 21)), initial_value=5, readonly=True, size=(5, 0), key='-QUESTION_COUNT-')],
        [sg.Text('使用する単語（カンマ区切り、オプション）:')],
        [sg.InputText(size=(30, 1), key='-USE_WORDS-')],
        [sg.Text('※ 使用する単語を指定しない場合は、一般的な語彙が使用されます。')],
        [sg.Button('開始'), sg.Button('キャンセル')]
    ]
    window = sg.Window(title='英会話練習アプリ', layout=layout)

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'キャンセル':
            window.close()
            exit()  # アプリを終了
        if event == '開始':
            cefr_level = values['-CEFR-'][0]
            speed = values['-SPEED-']
            question_count = values['-QUESTION_COUNT-']
            use_words = values['-USE_WORDS-'].split(',') if values['-USE_WORDS-'] else None
            window.close()
            return cefr_level, speed, question_count, use_words