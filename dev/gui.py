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

#Check if the current working directory is writable and accessible. 
# You can print the current working directory using os.getcwd().
print("Current Working Directory:", os.getcwd())

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
    widthMultiplier = 0.028 #0.038
    heightMultiplier = 0.015 #0.025

elif (1.60 < ratio < 1.69):
    widthMultiplier = 0.024 #0.034
    heightMultiplier = 0.011 #0.021

elif (1.7 < ratio < 1.79):
    widthMultiplier = 0.01 #0.03
    heightMultiplier = 0.07 #0.017

else:
    widthMultiplier = 0.025
    heightMultiplier = 0.015          

INPUT_BOX_SIZE = (round(widthMultiplier * w), round(heightMultiplier * h)) #round(0.6 * w), round(0.3 * h)) # width, height

lang = "English" # Default language 
display = "Wikipedia Article Comparison Tool" # Default title
colors = gen_colors() # Generate random colors for highlighting
pairs_source = {}
pairs_target = {}


# Section to select which language a user wants the display in the app screen
lang_selection = [
    # [sg.Text("")],
    # [
    #     sg.Push(),
    #     sg.Text("App Language:", key="-SELECT LANG-"), 
    #     sg.Combo(lang_eng, key="-LANG-", default_value="English", size = (10, 1)), 
    #     sg.Button("Select", key = "-SELECT-")
    # ]
    
]#end lang_selction

menu_def = [        #['Select comparison tool', 'Select similarity percentage']
    ['Help', 'User Guide'],
    ['Options', ['Select comparison tool', 'Select similarity percentage']],

 
    # Add ['\u2261'],'&App Language' this line to above line to have three lines for "hamburger menu"
] 

lang_selection = [
    [sg.Text("")],

    [sg.Menu(menu_def, tearoff=False, key = "-MENU")], # Add the Hamburger menu
     sg.Push(), sg.Text("App Language:", key="-SELECT LANG-"), sg.Combo(lang_eng, key="-LANG-", default_value="English", size=(10, 1)), 
     sg.Button("Select", key="-SELECT-")
]




text_entry = [
     [
       # sg.Push(),
       # sg.Push(),
      #  sg.Button("User Guide", key="-USER GUIDE-"),
        sg.Push(),
        sg.Push(),
    ],
    #sg.Push(),

    # Comparison and similarity score selection 
    [
        sg.Text("Select comparison tool:", key="-SELECT COMPARE TEXT-"),
        sg.Combo(["BLEU Score", "Sentence Bert"], key="-COMPARE SELECT-", default_value="BLEU Score"),
        sg.Text("Select similarity percentage:", key="-COMPARE VAL TEXT-"),
        sg.Slider(range=(1, 100), default_value=10, resolution=.01, orientation="h", key="-COMPARE VAL-"), # Default 1 -> 10 . I assigned resolution to .01
        sg.Button("Select", key="-SELECT COMPARE VALS-")
    ],

    # Link input box 
    [
        sg.Push(),
        #sg.Text('Source Article:'), sg.InputText('Paste your copied link here, and click Enter', key = '-LINK ENTERED-', size = (25, 1)), sg.Button('Enter'), 
        sg.Button("Source Article:", key="-SOURCE ARTICLE LANG-"), sg.InputText('Paste your link, and click Enter', key = '-LINK ENTERED-', size = (25, 1)), 
        sg.Button('Enter'), 
        #sg.Button("Source Article:", key="-USER GUIDE-"),
        sg.Push(),
        #sg.Text('Target Article:'), sg.Combo('', key = '-SAC CHOSEN-', default_value="Paste your copied link, and click Select!", size = (22, 1)), sg.Button("Select", key = "-CONFIRM SAC-"),
        sg.Button("Target Article:", key="-TARGET ARTICLE LANG-"), sg.Combo('', key = '-SAC CHOSEN-', default_value="Paste your link, Select language, and click Select", size = (22, 1)), 
        sg.Button("Select", key = "-CONFIRM SAC-"),
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
        sg.Push(),
        sg.Push(),
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
        sg.Push(),
        #sg.Button("Compare", key="-COMPARE-"), 
        sg.Button("Translate", key="-TRANSLATE-"),      #sg.Button("User Guide", key="-USER GUIDE-"),
        sg.Push(),
        #sg.Button("Translate", key="-TRANSLATE-"),
        sg.Button("Compare", key="-COMPARE-"),
    ],
]

# Setting the layout of the window
# THIS IS WHERE I WOULD ADD ADDITIONAL PARTS TO THE WINDOW AND ADD STYLING 
layout = [lang_selection, text_entry] 

window = sg.Window(title="Grey-Box Wikipedia Comparison",layout=layout, element_justification="c", resizable = True, font=("Arial", 18)).Finalize()
window.Maximize()

# Initializing variables for the link entered and the desired translation language link 
link = ""
linkTwoFragment = ""

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

def select_language():
    lang_selection_window = sg.Window("Select Language", [[sg.Text("Select your preferred language:")],
                        [sg.Combo(lang_eng, key="-LANG-", default_value="English", size=(20, 1))],
                                                         [sg.Button("OK")]])

   
  
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
        Update on screen display language to the selected language by a user.
        Language and matching translations are stored in a dictionary in languages.py
        '''
        if event == "-SELECT-" or event == 'Select comparison tool':
            lang = values["-LANG-"]
            print(lang)
            window["-SELECT LANG-"].update(display_trans[lang][0])
            window["-SELECT-"].update(display_trans[lang][1])
            window["-SOURCE ARTICLE LANG-"].update(display_trans[lang][14]) #[2] Ud
            window['-TARGET ARTICLE LANG-'].update(display_trans[lang][15]) #[2]
            #window['-LANG-'].update(display_trans[lang][2])
            window["-COMPARE-"].update(display_trans[lang][3])
            window["-SELECT COMPARE TEXT-"].update(display_trans[lang][4])
            window["-COMPARE VAL TEXT-"].update(display_trans[lang][5])
            window["-SELECT COMPARE VALS-"].update(display_trans[lang][1])
            window["-TRANSLATE-"].update(display_trans[lang][6])            #if window["-TRANSLATE-"].update(display_trans[lang][6])  
            window["-CLEAR-"].update(display_trans[lang][7])
            window["-WORD COUNT 1-"].update(display_trans[lang][8])
            window["-WORD COUNT 2-"].update(display_trans[lang][8])
            window["-TEXT SIM PERCENT 1-"].update(display_trans[lang][9])
            window["-TEXT SIM PERCENT 2-"].update(display_trans[lang][9]) 
         #   window["-USER GUIDE-"].update(display_trans[lang][16])

        '''
        Selecting comparison %
        The compare methods will search for sentences in Source and Target that have a similarity score GREATER THAN OR EQUAL TO this number
        '''
        sg.Push(),
        #sg.Text(""),
        if event == "-SELECT COMPARE VALS-":
            compare_type = values["-COMPARE SELECT-"]
            # Divide by 100 because comparison tools returns a value in [0, 1]
            sim_percent = int(values["-COMPARE VAL-"]) / 100

        file_path_text_1 = r"C:\Users\xiggy\OneDrive\Desktop\project-symmetry\project-symmetry\text1_download.txt"

        if event == "-SELECT DOWNLOAD CHOICE-":
            try:
                with open(file_path_text_1, "w", encoding="utf-8") as file:
                    file.write(values["-TEXT 1-"])
                print(f"Downloaded {dlOptions[0].lower()} text to: {file_path_text_1}")
                sg.popup('You downloaded your Source Article: Download complete!')
            except Exception as e:
                print(f"Error during download: {e}")

                
        file_path_text_2 = r"C:\Users\xiggy\OneDrive\Desktop\project-symmetry\project-symmetry\text2_download.txt"

        if event == "-SELECT DOWNLOAD CHOICE 2-":
            try:
                with open(file_path_text_2, "w", encoding="utf-8") as file:
                    file.write(values["-TEXT 2-"])
                print(f"Downloaded {dlOptions[1].lower()} text to: {file_path_text_2}")
             #   try:
               #     if()
              #      else
                sg.popup('You downloaded your Target Article: Download complete!')
            except Exception as e:
                print(f"Error during download: {e}")  

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
             #   window["-EXPAND SIM-"].update(visible=True)
                
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
                
                if len(target) > 4500 or len(target) == 4500:  
                    sg.popup_ok("Translation of article over 4500 WORDS may take long to translate- Please click OK to continue.", title="Warning: Long Translation Request")
            
                code = link.replace("https://", "")
                code = code.split('.')
                code = code[0]
                target = translate(code, target)
                window["-TEXT 2-"].update("")
                window["-TEXT 2-"].update(target)
              
        # Clear button
        if event == "-CLEAR-":
            window["-TEXT 1-"].update("")
            window["-TEXT 2-"].update("")
            window["-TEXT 1 WORD COUNT-"].update("")
            window["-TEXT 1 SIM PERCENT-"].update("")
            window["-TEXT 2 WORD COUNT-"].update("")
            window["-TEXT 2 SIM PERCENT-"].update("")
            window["-EXPAND SIM-"].update(visible=False)
        
        #User Guide button
        if event == 'User Guide':
            file = open("userguide.txt")
            user_guide = file.read()
            sg.popup_scrolled(user_guide, title="User Guide", font=("Arial", 18), size=(63, 18))

        if event == "-EXPAND SIM-":
            expand_list = []
            source_vals = list(pairs_source.values())
            target_vals = list(pairs_target.values())
            for i in range(0, len(source_vals)):
                expand_list.append(str(i+1) + ": SOURCE TEXT- " + target_vals[i][0] + "\nTARGET TEXT- " + source_vals[i][0] + "\n\n") #\n creates space for each line after, unsure how to fix, since cant use sep arg
            sg.popup_scrolled(' '.join(expand_list), title="Expanded View", font=("Arial", 18), size=(63, 18))
                	

        # Searching link events 
        if event == 'Enter':
            link = (values['-LINK ENTERED-'])
            print('The link submitted is: ' + link)
            languagesSACDict = scraper.languageGetter(link) # Dictionary for second language for article link (e.g.: [English - en,..中文 - zh]) 
            languagesSAC = list(languagesSACDict.keys())
            #print(languagesSAC) # Prints the available languages for checks and balances
            window['-SAC CHOSEN-'].update(values = languagesSAC, value = 'Paste your copied link here, and Click Select') #'Click here!'
            window["-TEXT 1-"].update(scraper.textGetter(link))

        if event == "-CONFIRM SAC-": 
            linkTwoFragment = (values['-SAC CHOSEN-'])
            print("The secondary language chosen is: " + linkTwoFragment)
            
            try:
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

        #if event in ('Select comparison tool', 'Select similarity percentage'):
        if event ==  'Select comparison tool':   #"-SELECT COMPARE TEXT-":
        # Add your logic here for handling these options
        # You may show a popup, prompt the user, or take other actions
            sg.popup(f'You selected: {event}')   
            select_language()

        if event == "Select similarity percentage":
            sg.popup(f'You selected: {event}')         
    window.close()

#end run
