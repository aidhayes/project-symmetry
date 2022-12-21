import deepl
from googletrans import Translator
from nltk.tokenize import sent_tokenize


auth_key = "0ff6b0ef-fc20-631e-6feb-695b9d666743:fx" 
deepl_trans = deepl.Translator(auth_key)
google_trans = Translator()
goog2 = ""

def translate_back(text2, goog2):
    text2_sent = sent_tokenize(text2)[0]
    goog2 = str(google_trans.detect(text2_sent).lang).upper()
    if goog2 == 'EN':
        goog2 = goog2 + '-US'

    result = deepl_trans.translate_text(text2, target_lang= goog2)

    return result
