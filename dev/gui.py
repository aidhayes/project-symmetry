from .translation import translate
from .translate_back import translate_back
import PySimpleGUI as sg # python3 -m pip install pysimplegui
from .ui.languages import lang_eng, display_trans
from .comparison.bleu_score import compare as bleu
from .comparison.bert import compare as bert
from nltk.tokenize import sent_tokenize
import numpy
from .ui.colors import gen_colors
from nltk.tokenize import sent_tokenize

INPUT_BOX_SIZE = (50, 25)
TITLE = 2
SELECT_LANG = 0
SELECT = 1
COMPARE = 3
SELECT_COMPARE = 4
SELECT_SIM = 5
CLEAR = 7
TRANSLATE = 6
lang = "English" # Default language 
display = "Wikipedia Article Comparison Tool" # Default title
colors = gen_colors()
# print(len(colors))

# Section to select which language a user wants the display in
lang_selection = [
    [
        sg.Push(), 
        sg.Text("Select Language:", key="-SELECT LANG-"), 
        sg.Combo(lang_eng, key="-LANG-", default_value="English"), 
        sg.Button("Select", key = "-SELECT-")]
]

# Title of application
welcome = [sg.Text(display, justification="c", key="-WELCOME-")]

# Text you want to compare
text_entry = [
    [
        sg.Text("Select comparison tool:", key="-SELECT COMPARE TEXT-"),
        sg.Combo(["BLEU Score", "Sentence Bert"], key="-COMPARE SELECT-", default_value="BLEU Score"),
        sg.Text("Select similarity percentage:", key="-COMPARE VAL TEXT-"),
        sg.Slider(range=(1, 100), default_value=1, resolution=.5, orientation="horizontal", key="-COMPARE VAL-"),
        sg.Button("Select", key="-SELECT COMPARE VALS-")
        ],

    [
        sg.Multiline(size=INPUT_BOX_SIZE, enable_events=True, key = "-TEXT 1-"),
        sg.Multiline(size=INPUT_BOX_SIZE, enable_events=True, key = "-TEXT 2-")
    ],

    [
        sg.Text("Word Count: ", key="-TEXT 1 WORD COUNT-"),
        sg.Text("Similarity Percentage: ", key="-TEXT 1 SIM PERCENT-"),
        sg.Push(),
        sg.Text("Word Count: ", key="-TEXT 2 WORD COUNT-"),
        sg.Text("Similarity Percentage: ", key="-TEXT 2 SIM PERCENT-")
    ],

    [ 
        # sg.Button("Translate Back", key="-TRANSLATE BACK-"),
        sg.Button("Clear", key="-CLEAR-"),
        sg.Button("Compare", key="-COMPARE-"),
        sg.Button("Translate", key="-TRANSLATE-")
    ]
]


# Setting the layout of the window
layout = [lang_selection, welcome, text_entry]

# Raj
window = sg.Window(title="Grey-Box Wikipedia Comparison",layout=layout, element_justification="c", font=("Arial", 20))
#If buttons are showing up on gui uncomment the code below and comment out the code above  
#window = sg.Window(title="Grey-Box Wikipedia Comparison", layout=layout, no_titlebar=False, location=(0,0), size=(800,600), keep_on_top=True, resizable=True, element_justification="c")

# Get word count of afrticle
# Yulong
def count_words(article):
    count = len(article.split()) #split string and return the length of list
    print(count)
    return count

# Similarity %
def percent_similar(article, sim_dict):
    sims_len = len(sim_dict)
    article_list = sent_tokenize(article)
    article_len = len(article_list)
    sim = (sims_len / article_len) * 100
    print(sim)
    return round(sim, 2)


# Clear Button
def clear():
    window["-TEXT 1-"].update("")
    window["-TEXT 2-"].update("") 

# Highlight the portions of text that are similar between the 2 articles
# Raj & Aidan
def highlight_sim(element, text, pairs):
    window[element].update("")
    sentences = sent_tokenize(text)
    for sentence in sentences:
        if sentence in pairs:
            window[element].update(sentence + " ", text_color_for_value="white", background_color_for_value = pairs[sentence][1], append=True)
        else:
            window[element].update(sentence + " ", text_color_for_value="green",background_color_for_value="black",  append=True)

# Highlight the portions of text that are different between the 2 articles
def highlight_diff(element, text, pairs):
    '''
        (Code goes here)
             ...
    '''

# Event loop
def run():
    compare_type = "BLEU Score" # Default comparison
    sim_percent = .3 # Default similarity score
    while True:

        event, values = window.read()

        # If user x's out of the window, then stop the application
        if event == sg.WIN_CLOSED:
            break
        
        # Update on screen text to the language the user selects
        if event == "-SELECT-":
            lang = values["-LANG-"]
            window["-SELECT LANG-"].update(display_trans[lang][SELECT_LANG])
            window["-SELECT-"].update(display_trans[lang][SELECT])
            window['-WELCOME-'].update(display_trans[lang][TITLE])
            window["-COMPARE-"].update(display_trans[lang][COMPARE])
            window["-SELECT COMPARE TEXT-"].update(display_trans[lang][SELECT_COMPARE])
            window["-COMPARE VAL TEXT-"].update(display_trans[lang][SELECT_SIM])
            window["-SELECT COMPARE VALS-"].update(display_trans[lang][SELECT])
            window["-CLEAR-"].update(display_trans[lang][CLEAR])
            window["-TRANSLATE-"].update(display_trans[lang][TRANSLATE])

        # Selecting comparison %
        if event == "-SELECT COMPARE VALS-":
            compare_type = values["-COMPARE SELECT-"]
            # Divide by 100 because comparison tools returns a value in [0, 1]
            sim_percent = int(values["-COMPARE VAL-"]) / 100

        # Comparing user inputted text
        if event == "-COMPARE-":
            # Getting text from multilines
            ref = values["-TEXT 1-"]
            hyp = values["-TEXT 2-"]
            

            window["-TEXT 1 WORD COUNT-"].update("Word Count: " + str(count_words(ref)))
            window["-TEXT 2 WORD COUNT-"].update("Word Count: " + str(count_words(hyp)))
            

            # Determining which comparison type is being user
            if compare_type == "BLEU Score":
                pairs_ref, pairs_hyp = bleu(ref, hyp, colors, sim_percent)
                window["-TEXT 1 SIM PERCENT-"].update("Similarity Percentage: " + str(percent_similar(ref, pairs_ref)) + "%")
                window["-TEXT 2 SIM PERCENT-"].update("Similarity Percentage: " + str(percent_similar(hyp, pairs_hyp)) + "%")
            elif compare_type == "Sentence Bert":
                pairs_ref, pairs_hyp = bert(ref, hyp, colors, sim_percent)
                window["-TEXT 1 SIM PERCENT-"].update("Similarity Percentage: " + str(percent_similar(ref, pairs_ref)) + "%")
                window["-TEXT 2 SIM PERCENT-"].update("Similarity Percentage: " + str(percent_similar(hyp, pairs_hyp)) + "%")
            # Highlight text based on results of comparison
            highlight_sim("-TEXT 1-", ref, pairs_ref)
            highlight_sim("-TEXT 2-", hyp, pairs_hyp)
            

        #Translate user inputted text
        if event == "-TRANSLATE-":
            text1 = values["-TEXT 1-"]
            text2 = values["-TEXT 2-"]
            text2 = translate(text1, text2)
            window["-TEXT 2-"].update("")
            window["-TEXT 2-"].update(text2)

        #Translate back to the origanl langs you put in
        if event == "-TRANSLATE BACK-":
            text2 = values["-TEXT 2-"]
            text2 = translate_back(text2, text2)
            window["-TEXT 2-"].update("")
            window["-TEXT 2-"].update(text2)
        
        #Clear Button
        if event == "-CLEAR-":
            window["-TEXT 1-"].update("")
            window["-TEXT 2-"].update("")


        



    window.close()

