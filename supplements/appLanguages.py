import csv
import requests as r
import collections
from bs4 import BeautifulSoup
collections.Callable = collections.abc.Callable
import appTranslator as aT
import itertools

# newline = '' stops blank lines between write
f = open('supplements/moreLanguages.csv', 'w', encoding="utf-8", newline = '')
f2 = open('supplements/missedLanguages.csv', 'w', encoding="utf-8", newline = '')
writer = csv.writer(f)
errorLogger = csv.writer(f2)
# Initialize language dictionary
languages = {}
# Texts needed to be translated for our display.csv

# 1) get all available languages on google translate, store them in dictionary with language code and languages
# List all divs under jsname = rPx1uf
translatePage = r.get('https://translate.google.com/')
soup = BeautifulSoup(translatePage.content, "html.parser")
list = soup.find("div", { "jsname" : "rPx1uf" }) 
children = list.findChildren("div", recursive = False)
for child in children:
    # Scraping the written out language name
    language = child.text
    language = language.replace('checkhistory', '')
    # Scraping the language code
    child = str(child)
    child = child.replace('<div class="qSb8Pe" data-language-code="', '')
    child = child.split('"', 1)
    del child[1]
    # List -> String, removing '[ and ]'
    languageCode = str(child)[2:-2]
    languages[languageCode] = language

del languages['<div class=']
#print(len(languages)) - 133 LANGUAGES - 18 translates each, 8hrs total

# Iterate through every available language
# Get the key and value from dictionary, specify that there are 2 things in the for loop

for key, value in languages.items():
    # Make a list to hold all translated pieces
    try:
        translatedList = [value, key]
        translatedList = translatedList + aT.translator(key)
        # Insert the new translated piece at the end of the list
        print(translatedList)
        # Write new row to our csv of 
        writer.writerow(translatedList)
        translatedList.clear()
        continue
    except: 
        # If there's an error translating a language, log said language in a csv
        errorLogger.writerow([key])
        continue

f.close()