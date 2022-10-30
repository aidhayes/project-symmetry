import PySimpleGUI as sg # python3 -m pip install pysimplegui
from languages import lang_eng, text
import bleu_score
from nltk.tokenize import sent_tokenize
from bert import bert

INPUT_BOX_SIZE = (50, 25)
TITLE = 2
SELECT_LANG = 0
SELECT = 1
COMPARE = 3
lang = "English"
display = "Wikipedia Article Comparison Tool"

def highlight_sim(element, text, pairs):
    window[element].update("")
    sentences = sent_tokenize(text)
    for sentence in sentences:
        if sentence in pairs:
            window[element].update(sentence + " ", text_color_for_value="white", background_color_for_value = pairs[sentence][1], append=True)
        else:
            window[element].update(sentence + " ", text_color_for_value="black", append=True)

lang_selection = [
    [sg.Push(), sg.Text("Select Language:", key="-SELECT LANG-"), sg.Combo(lang_eng, key="-LANG-", default_value="English"), sg.Button("Select", key = "-SELECT-")]
]

# Title of application
welcome = [sg.Text(display, justification="c", key="-WELCOME-")]

# Text you want to compare
text_entry = [
    [
        sg.Multiline(size=INPUT_BOX_SIZE, enable_events=True, key = "-TEXT 1-"),
        sg.Multiline(size=INPUT_BOX_SIZE, enable_events=True, key = "-TEXT 2-")
    ],
    [ 
        sg.Button("Compare", key="-COMPARE-")
    ]
]

# Setting the layout of the window
layout = [lang_selection, welcome, text_entry]
window = sg.Window(title="Grey-Box Wikipedia Comparison",layout=layout, element_justification="c", font=("Arial", 20))


# Event loop
while True:

    event, values = window.read()

    # If user x's out of the window, then stop the application
    if event == sg.WIN_CLOSED:
        break
    
    # Update on screen text to the language the user selects
    if event == "-SELECT-":
        lang = values["-LANG-"]
        window["-SELECT LANG-"].update(text[lang][SELECT_LANG])
        window["-SELECT-"].update(text[lang][SELECT])
        window['-WELCOME-'].update(text[lang][TITLE])
        window["-COMPARE-"].update(text[lang][COMPARE])
    
    if event == "-COMPARE-":
        ref = values["-TEXT 1-"]
        hyp = values["-TEXT 2-"]
        pairs_ref, pairs_hyp = bert.bert(ref, hyp)
        highlight_sim("-TEXT 1-", ref, pairs_ref)
        highlight_sim("-TEXT 2-", hyp, pairs_hyp)

window.close()

