import deepl
from googletrans import Translator
from nltk.tokenize import sent_tokenize

auth_key = "0ff6b0ef-fc20-631e-6feb-695b9d666743:fx" 
deepl_trans = deepl.Translator(auth_key)
google_trans = Translator()


def translate(text1, text2):
    text1_sent = sent_tokenize(text1)[0]
    goog = str(google_trans.detect(text1_sent).lang).upper()
    if goog == 'EN':
        goog = goog + '-US'

    result = deepl_trans.translate_text(text2, target_lang = goog) 
    
    return result


