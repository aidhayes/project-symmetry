import deepl
from googletrans import Translator


auth_key = "0ff6b0ef-fc20-631e-6feb-695b9d666743:fx" 
deepl_trans = deepl.Translator(auth_key)
google_trans = Translator()

def translate(text1, text2):
    
    goog = str(google_trans.detect(text1).lang).upper()
    if goog == 'EN':
        goog = goog + '-US'

    result = deepl_trans.translate_text(text2, target_lang = goog) 
    
    return result





'''
if lang = eng
    lang = lang + '-us'

'''


#make this into a mehtod
#do a def method that takes text1 and text2 as parms
#put everything into the method
#get rid of the print methods and return result
#set text in the gui in the translate method setting the text on the left side to whatever the txt is on the right side
#if lang is english append '-US'
