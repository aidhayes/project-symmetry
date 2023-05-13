from .translation import translate
import PySimpleGUI as sg
#from .ui.languages import lang_eng, display_trans
from .comparison.bleu_score import compare as bleu
from .comparison.bert import compare as bert
from nltk.tokenize import sent_tokenize
from .ui.colors import gen_colors
from nltk.tokenize import sent_tokenize
import nltk
import requests
import dev.scraper as scraper
import csv
import sys
import os

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
Aidan Hayes, Raj Jagroup, Joseph LaBianca, Yulong Chen - Fall 2022
Jin Long Shi, Alden Strafford, Henry Qiu, Yuhao Wang, Ambrose Ngayinoko - Spring 2023
'''

if not nltk.data.find("tokenizers/punkt"):
    nltk.download('punkt')

#For exe- uncomment below line
#bundle_dir = getattr(sys, '_MEIPASS', os.path.abspath(os.path.dirname(__file__)))
#For exe- replace line 46 (open moreLang csv) with below line and uncomment line 390 and comment out line 391 (userguide open)
#with open(os.path.abspath(os.path.join(bundle_dir, "moreLanguagesFinal.csv")), 'r', encoding = "utf-8") as file:

display_trans = {}
lang_eng = []
with open("./supplements/moreLanguagesFinal.csv", 'r', encoding = "utf-8") as file:
    for line in csv.reader(file):
        display_trans[line[0]] = line[2:]
        lang_eng.append(line[0])

dlOptions = ['Source', 'Target']

dlImg = b'iVBORw0KGgoAAAANSUhEUgAAADMAAAA7CAYAAADW8rJHAAAAAXNSR0IArs4c6QAAAoBJREFUaEPtmW3OwUAQx6dEKhLEyw1wBgfwwdsBnNEFvB3BFfQKmiARkbBPWk+l2LYzuzt4nqyvpjPz+8/s2A4HeD9C4t7hCsnmGACEEK8sjhOGZInL4jQJJKoIF5CFQfS8tMVsZRDK3UUi2FJMbWUoasls7QBAKGjbDCFSqoltM4SCts0QItk20xXJtpmugnaaIRS0bYYQyU4zXZFsm+kqaKcZQsE/02bxZVhSZXVgMP6lelLb7CHJlP2XKgzWvzYMZUOpAkPxrwVDTY7bng8mXB4/7pApMKm2Et+J8wd7ZjIDPgXFwlD9GrnOoILGgIK/AJIVvFUx1Sb+MHbRjq3Mb+zkBBG/PUomWJBQSGIEdIWIfqXm4/EYZrMZOke0YSzaW4CoICqViZhYgVRAdGDYztBoNIL5fK7SMQ9n5vl0YxwarRABRJprlPBLUoQpYgSIAvI89qNcA5jEZN4FNBwOYbFYaHVCkKvTarWE53nS0djpdMDzPEwQ5TNEAIF2uy02m438XhbAuK4rTqeT1KDRaIDv+1gYMhAFJHBer9fFdruV5losFsEpFArifD6bgkED9ft9WK1WFKFSYVzXZYHJBFIByaoMJ0wi0GAwgOVySapI1DZpbcYN8wJEmI7Stv80TAgUy0ypIt9SGROX57uPb6iMMSALE0lZrVZhv99r9bmxsgBApVIRu91O6jJzmuVyOSiVSpDP503mpOTrcrnA8XiE6/WqBqMU9UMPZVbmQ3kphf1/MLVaTfi+r6TGNz0U3PBTX86+KdmsXCaTyX0HYOTVNysg1/fdbhfW6/XvnvQWRTSbTTgcDtESnCu2Eb/BHqBcLkOv14PpdBr+Fv4A8cnJcCg/vWQAAAAOZVhJZk1NACoAAAAIAAAAAAAAANJTkwAAAABJRU5ErkJggg=='

#resizing window functionality- should work, not tested very heavily though
w, h = sg.Window.get_screen_size()
ratio = round(w/h, 2)
widthMultiplier = .01
heightMultiplier = .01
if (0.00 < ratio < 1.59):
    widthMultiplier = 0.038
    heightMultiplier = 0.025

elif (1.60 < ratio < 1.69):
    widthMultiplier = 0.034
    heightMultiplier = 0.021

elif (1.7 < ratio < 1.79):
    widthMultiplier = 0.03
    heightMultiplier = 0.017

else:
    widthMultiplier = 0.025
    heightMultiplier = 0.015          

INPUT_BOX_SIZE = (round(widthMultiplier * w), round(heightMultiplier * h)) #round(0.6 * w), round(0.3 * h)) # width, height
# 1 character = 10 pixels wide, 1 row = 20 pixels high
# if ratio of length to width is c1 < x < c2, make input box size y * w z * h, etc.

lang = "English" # Default language 
display = "Wikipedia Article Comparison Tool" # Default title
colors = gen_colors() # Generate random colors for highlighting
pairs_source = {}
pairs_target = {}

# Section to select which language a user wants the display in

lang_selection = [
    [
        sg.Text("")
    ],

    [
        sg.Push(),
        sg.Text("App Language:", key="-SELECT LANG-"), 
        sg.Combo(lang_eng, key="-LANG-", default_value="English", size = (10, 1)), 
        sg.Button("Select", key = "-SELECT-")
    ]
    
]

# Title of application
#welcome = [sg.Text(display, justification="c", key="-WELCOME-")]

#sg.theme('DarkAmber') #color of text, eventually we will have the color be f(userSelectedColor) 

text_entry = [

    # Comparison and similarity score selection 
    [
        sg.Text("Select comparison tool:", key="-SELECT COMPARE TEXT-"),
        sg.Combo(["BLEU Score", "Sentence Bert"], key="-COMPARE SELECT-", default_value="BLEU Score"),
        sg.Text("Select similarity percentage:", key="-COMPARE VAL TEXT-"),
        sg.Slider(range=(1, 100), default_value=10, resolution=.5, orientation="horizontal", key="-COMPARE VAL-"), # Default 1 -> 10 
        sg.Button("Select", key="-SELECT COMPARE VALS-")
    ],

    # Link input box 
    [
        sg.Push(),
        sg.Text('Source Article:'), sg.InputText('https://en.wikipedia.org/wiki/Wikipedia:Example', key = '-LINK ENTERED-', size = (25, 1)), sg.Button('Enter'), 
        sg.Push(),
        sg.Text('Target Article:'), sg.Combo('', key = '-SAC CHOSEN-', default_value="Enter a link first!", size = (22, 1)), sg.Button("Select", key = "-CONFIRM SAC-"),
        sg.Push()
    ],

    # Text you want to compare
    [ 
        sg.Multiline(size=INPUT_BOX_SIZE, enable_events=True, key = "-TEXT 1-"),
        sg.Multiline(size=INPUT_BOX_SIZE, enable_events=True, key = "-TEXT 2-")
    ],
    
    [ 
        sg.Text('')
    ],

# Statistics display
    [
        sg.Text("Word Count: ", key="-WORD COUNT 1-"),
        sg.Text(" ", key="-TEXT 1 WORD COUNT-"),
        sg.Text("Similarity Percentage: ", key="-TEXT SIM PERCENT 1-"),
        sg.Text(" ", key="-TEXT 1 SIM PERCENT-"),

        sg.Push(),

        sg.Button('', image_data=dlImg, border_width = 25,
            button_color=(sg.theme_background_color(),sg.theme_background_color()),
            key="-SELECT DOWNLOAD CHOICE-"),
        sg.Push(),
        sg.Push(),
        sg.Push(),
        sg.Push(),
        sg.Push(),
        sg.Button('', image_data=dlImg, border_width=25, 
            button_color=(sg.theme_background_color(),sg.theme_background_color()),
            key="-SELECT DOWNLOAD CHOICE 2-"),

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
    ],

    [
        sg.Push(),
        sg.Button("User Guide", key="-USER GUIDE-")
    ]
]

# Setting the layout of the window
# THIS IS WHERE I WOULD ADD ADDITIONAL PARTS TO THE WINDOW AND ADD STYLING 
layout = [lang_selection, text_entry] #welcome, text_entry]

window = sg.Window(title="Grey-Box Wikipedia Comparison",layout=layout, element_justification="c", resizable = True, font=("Arial", 18)).Finalize()
window.Maximize()

# Initializing variables for the link entered and the desired translation language link 
link = ""
linkTwoFragment = ""

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
#def clear():
    #window["-TEXT 1-"].update("")
    #window["-TEXT 2-"].update("") 

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
    
    folderChoice = ''
    compare_type = "BLEU Score" # Default comparison type 
    sim_percent = .1 # Default similarity score //Doesn't work 
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
            print(lang)
            window["-SELECT LANG-"].update(display_trans[lang][0])
            window["-SELECT-"].update(display_trans[lang][1])
            #window['-WELCOME-'].update(display_trans[lang][2])
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
            #window["-SOURCE-"].update(display_trans[lang][14])
            #window["-TARGET-"].update(display_trans[lang][15])
            window["-USER GUIDE-"].update(display_trans[lang][16])

        '''
        Selecting comparison %
        The compare methods will search for sentences in Source and Target that have a similarity score GREATER THAN OR EQUAL TO this number
        '''
        if event == "-SELECT COMPARE VALS-":
            compare_type = values["-COMPARE SELECT-"]
            # Divide by 100 because comparison tools returns a value in [0, 1]
            sim_percent = int(values["-COMPARE VAL-"]) / 100
        
        if event == "-SELECT DOWNLOAD CHOICE-":
            f = open("myfile.txt", "w")
            print(f"Downloading {dlOptions[0].lower()} text to default directory since nothing was chosen")
            f.write(values["-TEXT 1-"])
            f.close()

        if event == "-SELECT DOWNLOAD CHOICE 2-":
            f = open("myfile.txt", "w")
            print(f"Downloading {dlOptions[1].lower()} text to default directory since nothing was chosen")
            f.write(values["-TEXT 2-"])
            f.close()

        # Comparing user inputted text
        if event == "-COMPARE-":
            # Retrieve text from text boxes
            source = values["-TEXT 1-"]
            target = values["-TEXT 2-"]
            


            # Display word count for each article
            window["-TEXT 1 WORD COUNT-"].update(str(count_words(source)))
            window["-TEXT 2 WORD COUNT-"].update(str(count_words(target)))
            

            # Determining which comparison type is being used
            try:
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
                window["-EXPAND SIM-"].update(visible=True)
                # Highlight text based on results of comparison
                highlight_sim("-TEXT 1-", source, pairs_source)
                highlight_sim("-TEXT 2-", target, pairs_target)
            except ZeroDivisionError:
                sg.popup_ok("Must have text in both source and target to perform compare operation.", title="ERROR: MISSING TEXT!")
            

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
                #if len(target) < 4500: can change this if to try and except to the popups below
                if(len(target) > 4500):
                    sg.popup_ok("Translation of article over 4500 words may take long to translate- please wait.", title="Warning: Long Translate Request")
                #try:
                code = link.replace("https://", "")
                code = code.split('.')
                code = code[0]
                target = translate(code, target)
                window["-TEXT 2-"].update("")
                window["-TEXT 2-"].update(target)
                #except:
                #    try:
                #        sg.Popup(display_trans[lang][13], keep_on_top=True, title= display_trans[lang][12])
                #    except:
                #       sg.Popup(display_trans["English"][13], keep_on_top=True, title= display_trans["English"][12])


        # NOT IMPLEMENTED
        #if event == "-TRANSLATE BACK-":
         #   text2 = values["-TEXT 2-"]
          #  text2 = translate_back(text2, text2)
           # window["-TEXT 2-"].update("")
            #window["-TEXT 2-"].update(text2)
        
        # Clear button
        if event == "-CLEAR-":
            window["-TEXT 1-"].update("")
            window["-TEXT 2-"].update("")
            window["-TEXT 1 WORD COUNT-"].update("")
            window["-TEXT 1 SIM PERCENT-"].update("")
            window["-TEXT 2 WORD COUNT-"].update("")
            window["-TEXT 2 SIM PERCENT-"].update("")
            window["-EXPAND SIM-"].update(visible=False)

        if event == "-USER GUIDE-":
            #file = open(os.path.abspath(os.path.join(bundle_dir, "userguide.txt"))) For exe- uncomment this line and comment out below line 
            file = open("userguide.txt")
            user_guide = file.read()
            sg.popup_scrolled(user_guide, title="User Guide", font=("Arial", 18), size=(63, 18))

        #expand view- shows matching sentences in popup- renaming it was discussed, so dont hesitate to change the name to something you think is more fitting
        if event == "-EXPAND SIM-":
            expand_list = []
            source_vals = list(pairs_source.values())
            target_vals = list(pairs_target.values())
            for i in range(0, len(source_vals)):
                expand_list.append(str(i+1) + ": SOURCE TEXT- " + target_vals[i][0] + "\nTARGET TEXT- " + source_vals[i][0] + "\n\n") #\n creates space for each line after, unsure how to fix, since cant use sep arg
            sg.popup_scrolled(' '.join(expand_list), title="Expanded View", font=("Arial", 18), size=(63, 18))
            #for i in range(0, len(source_vals)):
            #, text_color_for_value="white", background_color_for_value=source_vals[i][1], append=True        	

        # Searching link events 
        if event == 'Enter':
            link = (values['-LINK ENTERED-'])
            print('The link submitted is: ' + link)
            languagesSACDict = scraper.languageGetter(link) # Dictionary for second language for article link (e.g.: [English - en,..中文 - zh]) 
            languagesSAC = list(languagesSACDict.keys())
            #print(languagesSAC) # Prints the available languages for checks and balances
            window['-SAC CHOSEN-'].update(values = languagesSAC, value = 'Click here!')
            window["-TEXT 1-"].update(scraper.textGetter(link))

        if event == "-CONFIRM SAC-": 
            linkTwoFragment = (values['-SAC CHOSEN-'])
            print("The secondary language chosen is: " + linkTwoFragment)
            # Only if the link was entered will this work, exception handling a crash 

            try:
                #link = link.replace("https://", "")
                #linkList = link.split(".", 1)
                #linkTwo = "https://" + languagesSACDict[linkTwoFragment] + "." + linkList[1]
                linkTwo = languagesSACDict[linkTwoFragment]
                print(linkTwo)
                response = requests.get(linkTwo)
                """
                IMPLEMENT ERROR HANDLING FOR IF NO INTERNET
                """
                if (response.status_code == 200):
                    print(f"The article's secondary language link is {linkTwo}\nThe response from the server is: {response.status_code}, meaning the webpage exists!")

                elif (response.status_code == 404): 
                    print(f"Sorry, this article does not exist in {linkTwoFragment}\nThe response from the server is {response.status_code}, meaning the webpage does not exist!")
                window["-TEXT 2-"].update(scraper.textGetter(linkTwo))

            except:
                print("No link entered or no language chosen")
                
    window.close()

