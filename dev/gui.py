from .translation import translate
from .translate_back import translate_back
import PySimpleGUI as sg # python3 -m pip install pysimplegui
from .ui.languages import lang_eng, display_trans
from .comparison.bleu_score import compare as bleu
from .comparison.bert import compare as bert
from nltk.tokenize import sent_tokenize
from .ui.colors import gen_colors
from nltk.tokenize import sent_tokenize

'''
GUI file that designs the GUI of the application using PySimpleGUI

For more information visit https://www.pysimplegui.org/en/latest/

The GUI includes:
    - On screen language selection
    - Comparison tool selection
    - Text boxes for the Source and Target articles to be copy/pasted into
    - Button to clear both text boxes
    - Button to compare the Source and Target articles
    - Button to translate the Target to match the language of the Source
More information on "Source" and "Target" can be found in bleu_score.py and bert.py

Contributors:
Aidan Hayes, Raj Jagroup, Joseph LaBianca, Yulong Chen
'''

INPUT_BOX_SIZE = (50, 25) # Size of text box

lang = "English" # Default language 
display = "Wikipedia Article Comparison Tool" # Default title
colors = gen_colors() # Generate random colors for highlighting

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


text_entry = [

    # Comparison and similarity score selection 
    [
        sg.Text("Select comparison tool:", key="-SELECT COMPARE TEXT-"),
        sg.Combo(["BLEU Score", "Sentence Bert"], key="-COMPARE SELECT-", default_value="BLEU Score"),
        sg.Text("Select similarity percentage:", key="-COMPARE VAL TEXT-"),
        sg.Slider(range=(1, 100), default_value=1, resolution=.5, orientation="horizontal", key="-COMPARE VAL-"),
        sg.Button("Select", key="-SELECT COMPARE VALS-")
    ],

    [
        sg.Text("Source", key="-SOURCE-"),

        # Centering of labels, perhaps there is a better way... seems to work for now
        sg.Text("\t"),
        sg.Text("\t"),
        sg.Text("\t"),
        sg.Text("\t"),
        sg.Text("\t"),

        sg.Text("Target", key="-TARGET-"),
    ],
    # Text you want to compare
    [ 
        sg.Multiline(size=INPUT_BOX_SIZE, enable_events=True, key = "-TEXT 1-"),
        sg.Multiline(size=INPUT_BOX_SIZE, enable_events=True, key = "-TEXT 2-")
    ],

    # Statistics display
    [
        sg.Text("Word Count: ", key="-WORD COUNT 1-"),
        sg.Text(" ", key="-TEXT 1 WORD COUNT-"),
        sg.Text("Similarity Percentage: ", key="-TEXT SIM PERCENT 1-"),
        sg.Text(" ", key="-TEXT 1 SIM PERCENT-"),
        sg.Push(),
        sg.Text("Word Count: ", key="-WORD COUNT 2-"),
        sg.Text(" ", key="-TEXT 2 WORD COUNT-"),
        sg.Text("Similarity Percentage: ", key="-TEXT SIM PERCENT 2-"),
        sg.Text(" ", key="-TEXT 2 SIM PERCENT-")
    ],

    # Buttons for clear, compare, and translate
    [ 
        # sg.Button("Translate Back", key="-TRANSLATE BACK-"),
        sg.Button("Clear", key="-CLEAR-"),
        sg.Button("Compare", key="-COMPARE-"),
        sg.Button("Translate", key="-TRANSLATE-")
    ]
]


# Setting the layout of the window
layout = [lang_selection, welcome, text_entry]

window = sg.Window(title="Grey-Box Wikipedia Comparison",layout=layout, element_justification="c", font=("Arial", 18))

# If buttons are showing up on gui uncomment the code below and comment out the code above  
#window = sg.Window(title="Grey-Box Wikipedia Comparison", layout=layout, no_titlebar=False, location=(0,0), size=(800,600), keep_on_top=True, resizable=True, element_justification="c")

# Get word count of article
def count_words(article):
    count = len(article.split()) #split string and return the length of list
    print(count)
    return count

'''
Calculate the similarity percentage of one article to the other
Similarity percentage is calculated using:
(# similar sentences) / (# total sentences) * 100
Result is rounded to nearest hundreth
'''
def percent_similar(article, sim_dict):
    sims_len = len(sim_dict)
    article_list = sent_tokenize(article)
    article_len = len(article_list)
    sim = (sims_len / article_len) * 100
    print(sim)
    return round(sim, 2)


# Clear the text from both text boxes
def clear():
    window["-TEXT 1-"].update("")
    window["-TEXT 2-"].update("") 

# Highlight the portions of text that are similar between the 2 articles
# Sentences that are similar will be highlighted with the same color
# More information on how finding similarities can be found in bleu_score.py and bert.py
def highlight_sim(element, text, pairs):
    window[element].update("")
    sentences = sent_tokenize(text)
    for sentence in sentences:
        # Highlight similarities
        if sentence in pairs:
            window[element].update(sentence + " ", text_color_for_value="white", background_color_for_value = pairs[sentence][1], append=True)
        # Highlight differences
        else:
            window[element].update(sentence + " ", text_color_for_value="green",background_color_for_value="black",  append=True)

# Highlight the portions of text that are different between the 2 articles
def highlight_diff(element, text, pairs):
    '''
        (Code goes here)
             ...
    '''

'''
Event loop
Reads for on screen events performed by the user
'''
def run():
    compare_type = "BLEU Score" # Default comparison type 
    sim_percent = .3 # Default similarity score
    while True:

        # The event performed by the user and any value returned by performing that event
        event, values = window.read()

        # If user x's out of the window, then stop the application
        if event == sg.WIN_CLOSED:
            break
        
        '''
        Update on screen display language to the selected language by a user
        Language and matching translations are stored in a dictionary in languages.py
        '''
        if event == "-SELECT-":
            lang = values["-LANG-"]
            window["-SELECT LANG-"].update(display_trans[lang][0])
            window["-SELECT-"].update(display_trans[lang][1])
            window['-WELCOME-'].update(display_trans[lang][2])
            window["-COMPARE-"].update(display_trans[lang][3])
            window["-SELECT COMPARE TEXT-"].update(display_trans[lang][4])
            window["-COMPARE VAL TEXT-"].update(display_trans[lang][5])
            window["-SELECT COMPARE VALS-"].update(display_trans[lang][1])
            window["-TRANSLATE-"].update(display_trans[lang][6])
            window["-CLEAR-"].update(display_trans[lang][7])
            window["-WORD COUNT 1-"].update(display_trans[lang][8])
            window["-WORD COUNT 2-"].update(display_trans[lang][8])
            window["-TEXT SIM PERCENT 1-"].update(display_trans[lang][9])
            window["-TEXT SIM PERCENT 2-"].update(display_trans[lang][9])
            window["-SOURCE-"].update(display_trans[lang][14])
            window["-TARGET-"].update(display_trans[lang][15])

        '''
        Selecting comparison %
        The compare methods will search for sentences in Source and Target that have a similarity score GREATER THAN OR EQUAL TO this number
        '''
        if event == "-SELECT COMPARE VALS-":
            compare_type = values["-COMPARE SELECT-"]
            # Divide by 100 because comparison tools returns a value in [0, 1]
            sim_percent = int(values["-COMPARE VAL-"]) / 100

        # Comparing user inputted text
        if event == "-COMPARE-":
            # Retrieve text from text boxes
            source = values["-TEXT 1-"]
            target = values["-TEXT 2-"]
            


            # Display word count for each article
            window["-TEXT 1 WORD COUNT-"].update(str(count_words(source)))
            window["-TEXT 2 WORD COUNT-"].update(str(count_words(target)))
            

            # Determining which comparison type is being used
            if compare_type == "BLEU Score":
                pairs_source, pairs_target = bleu(source, target, colors, sim_percent)
                # Display similarity % of articles
                window["-TEXT 1 SIM PERCENT-"].update(str(percent_similar(source, pairs_source)) + "%")
                window["-TEXT 2 SIM PERCENT-"].update(str(percent_similar(target, pairs_target)) + "%")
            elif compare_type == "Sentence Bert":
                pairs_source, pairs_target = bert(source, target, colors, sim_percent)
                # Display similarity % of articles
                window["-TEXT 1 SIM PERCENT-"].update(str(percent_similar(source, pairs_source)) + "%")
                window["-TEXT 2 SIM PERCENT-"].update(str(percent_similar(target, pairs_target)) + "%")
            # Highlight text based on results of comparison
            highlight_sim("-TEXT 1-", source, pairs_source)
            highlight_sim("-TEXT 2-", target, pairs_target)
            

        # Translate user inputed text
        # Text from the "Target" box is translated to match the language in the "Source" box
        if event == "-TRANSLATE-":

            source = values["-TEXT 1-"]
            target = values["-TEXT 2-"]
            if len(source) == 0:
                try:
                    sg.Popup(display_trans[lang][11], keep_on_top=True, title= display_trans[lang][10])
                except:
                    sg.Popup(display_trans["English"][11], keep_on_top=True, title= display_trans["English"][10])
            else:
                if len(target) < 4500:
                    target = translate(source, target)
                    window["-TEXT 2-"].update("")
                    window["-TEXT 2-"].update(target)
                else:
                    try:
                        sg.Popup(display_trans[lang][13], keep_on_top=True, title= display_trans[lang][12])
                    except:
                        sg.Popup(display_trans["English"][13], keep_on_top=True, title= display_trans["English"][12])

        # Translate back to the origanl language you put in
        # NOT IMPLEMENTED
        if event == "-TRANSLATE BACK-":
            text2 = values["-TEXT 2-"]
            text2 = translate_back(text2, text2)
            window["-TEXT 2-"].update("")
            window["-TEXT 2-"].update(text2)
        
        # Clear button
        if event == "-CLEAR-":
            window["-TEXT 1-"].update("")
            window["-TEXT 2-"].update("")

    window.close()

