#This is the translation method which uses deepl and google_trans
#to translate the target article (right) to whatever language the 
#source article (left) is in

import deepl
from googletrans import Translator
from nltk.tokenize import sent_tokenize

#here is the auth_key which connects to deepl allowing us to be able to translate
#google_trans helps with the language codes
auth_key = "0ff6b0ef-fc20-631e-6feb-695b9d666743:fx" 
deepl_trans = deepl.Translator(auth_key)
google_trans = Translator()

# What is this doing right here is reading what language the source article
# using google_trans.detect to figure out the language code which in term
# allows deepl to translate the target article
# Contributor: Joe LaBianca
def translate(text1, text2):
    text1_sent = sent_tokenize(text1)[0]
    goog = str(google_trans.detect(text1_sent).lang).upper()
    if goog == 'EN': #here since some language have different versions like english and british english we had to make sure that is always US english
        goog = goog + '-US'
    if goog == 'PT': #same goes for portuguese 
        goog = goog + '-BR'

    result = deepl_trans.translate_text(text2, target_lang = goog) 
    
    return result


