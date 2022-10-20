import csv

text = dict()

with open("display.csv") as file:
    for line in csv.reader(file):
        text[line[0]] = line[2:]
        
lang_eng = [ 
            "Arabic",
            "Bangla",
            "Bulgarian",
            "Bosnian",
            "Catalan",
            "Czech",
            "Danish",
            "German",
            "Estonian",
            "Greek",
            "Spanish",
            "Esperanto",
            "Basque",
            "Persian",
            "French",
            "Galician",
            "Korean",
            "Croatian",
            "Indonesian",
            "Italian",
            "Hebrew",
            "Georgian",
            "Latvian",
            "Lithuanian",
            "Hungarian",
            "Macedonian",
            "Malay",
            "Dutch",
            "Japanese",
            "Norwegian Bokmål",
            "Polish",
            "Portugese",
            "Romanian",
            "Russian",
            "English",
            "Slovak",
            "Slovenian",
            "Serbian",
            "Finnish",
            "Swedish",
            "Thai",
            "Turkish",
            "Ukranian",
            "Vietnamese",
            "Chinese"

        ]

