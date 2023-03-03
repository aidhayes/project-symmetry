import requests
import collections
from bs4 import BeautifulSoup
collections.Callable = collections.abc.Callable

page = requests.get('https://en.wikipedia.org/wiki/Barack_Obama')
#test = fromstring(r.text)
soup = BeautifulSoup(page.content, "html.parser") #ensures we are using the right parser for our HTML document
results = soup.find(id="p-lang-btn")
languages = results.find_all("li", class_="interlanguage-link")

for htmlListItem in languages:
    language = htmlListItem.get_text() # Gets the text of the HTML element
    link = htmlListItem.find('a')
    #print(language, end = "\n")
    link = str(link)
    link = link.split('.') # Splits the string up into a list by the "."
    # for item in link if it contains https then link = link[x]
    for listItem in link: # Iterates through the current HTML list item
        if "https:" in listItem: # We are looking for the list item in link that contains the new language abbreviation
            link = listItem # The overall link list will be replaced by just this string
        else:
            continue
    link = link.split('https://')
    link.pop(0)
    link = str(link[0])
    print(link, end="\n"*2) # end always attaches the same thing to the ending of a print statement