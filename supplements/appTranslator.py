import csv
import time
import pandas as pd
from selenium import webdriver 
from selenium.webdriver import Chrome 
from selenium.webdriver.chrome.service import Service 
from selenium.webdriver.common.by import By 
from webdriver_manager.chrome import ChromeDriverManager

def translator(shortLanguage):
    # Texts needed to be translated for our display.csv
    translators = ['Select%20Language%3A','Select','Wikipedia%20Article%20Comparison%20Tool','Compare','Select%20comparison%20tool%3A',
    'Select%20similarity%20percentage%3A','Translate','Clear','Word%20Count%3A','Similarity%20Percentage%3A','ERROR%3A%20NO%20TEXT%20IN%20SOURCE%20BOX!',
    'In%20order%20to%20translate%2C%20text%20is%20needed%20in%20the%20Source%20box%20so%20that%20the%20text%20in%20the%20Target%20box%20can%20be%20translated%20to%20match.',
    'ERROR%3A%20Too%20many%20characters','The%20length%20of%20text%20you%20are%20trying%20to%20translate%20exceeds%20the%20character%20limit%20of%204500.','Source','Target']

    # start by defining the options 
    options = webdriver.ChromeOptions() 
    options.add_argument('--headless') # it's more scalable to work in headless mode 
    options.add_argument("--log-level=3") # mutes console log unless it's of level 3: URGENT
    # normally, selenium waits for all resources to download - don't need to as we only need text content
    options.page_load_strategy = 'none' 
    # returns path to web driver downloaded 
    chrome_path = ChromeDriverManager().install() 
    chrome_service = Service(chrome_path) 
    # pass the defined options and service objects to initialize the web driver 
    driver = Chrome(options=options, service=chrome_service) 
    driver.implicitly_wait(5)
    print(len(translators))
    # Make a list to hold all translated pieces
    translatedList = []
    for element in translators:
        url = f'https://translate.google.com/?sl=en&tl={shortLanguage}&text={element}&op=translate'
        print(url)
        driver.get(url)
        time.sleep(4)
        content = driver.find_element(By.CSS_SELECTOR, "div[class*='lRu31'")
        # Insert the new translated piece at the end of the list
        translatedList.insert (len(translatedList), content.text) 
    return translatedList