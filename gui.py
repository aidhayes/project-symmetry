import PySimpleGUI as sg # python3 -m pip install pysimplegui
from languages import lang_eng

INPUT_BOX_SIZE = (50, 25)
lang = "English"
lang_selection = [
    [sg.Push(), sg.Text("Select a language:"), sg.Combo(lang_eng, key="-LANG-"), sg.Button("Select")]
]

# Title of application
welcome = [sg.Text("Wikipedia Article Comparison Tool", justification="c")]

# Text you want to compare
text_entry = [
    [
        sg.Multiline(size=INPUT_BOX_SIZE, enable_events=True, key = "-TEXT 1-"),
        sg.Multiline(size=INPUT_BOX_SIZE, enable_events=True, key = "-TEXT 2-")
    ],
    [ 
        sg.Button("Compare")
    ]
]

# Setting the layout of the window
layout = [lang_selection, welcome, text_entry]
window = sg.Window(title="Grey-Box Wikipedia Comparison",layout=layout, element_justification="c")


# Event loop
while True:
    event, values = window.read()
    # If user x's out of the window, then stop the application
    if event == sg.WIN_CLOSED:
        break
    
    if event == "Select":
        lang = values["-LANG-"]

    print(lang)

window.close()