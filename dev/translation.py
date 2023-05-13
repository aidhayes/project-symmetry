#This is the translation method which uses deepl and google_trans
#to translate the target article (right) to whatever language the 
#source article (left) is in
import math
import deepl
from nltk.tokenize import sent_tokenize
from textwrap import wrap

#here is the auth_key which connects to deepl allowing us to be able to translate
#google_trans helps with the language codes
auth_key = "0ff6b0ef-fc20-631e-6feb-695b9d666743:fx" #this is specifically valentin/grey-box api key- it is a free key that allows 500k chars translated a month
#whoever takes over- discuss with valentin best option- either paid version of deepl, or another translation api
deepl_trans = deepl.Translator(auth_key)

# allows deepl to translate the target article
# Contributor: Joe LaBianca, Raj JaGroup

deeplLangs = [
    "BG", "CS", "DA", "DE", "EL", "EN", "EN-GB", "EN-US", "ES", "ET", "FI", "FR", "HU", "ID", "IT", "JA", "KO", "LT", "LV", "NB", "NL", "PL", "PT", "PT-BR", "PT-PT", "RO", "RU", "SK", "SL", "SV", "TR", "UK", "ZH"
]
"""
"BG" : 'bg',
"CS" : 'cs',
"DA" : 'da',
"DE" : 'de',
"EL" : 'el',
"EN" : English,
"EN-GB" : English (British),
"EN-US" : English (American),
"ES" : Spanish,
"ET" : Estonian,
"FI" : Finnish,
"FR" : French,
"HU" : Hungarian,
"ID" : Indonesian,
"IT" : Italian,
"JA" : Japanese,
"KO" : Korean,
"LT" : Lithuanian,
"LV" : Latvian,
"NB" : Norwegian (Bokmål),
"NL" : Dutch,
"PL" : Polish,
"PT" : Portuguese (unspecified variant for backward compatibility; please select PT-BR or PT-PT instead),
PT-"BR" : Portuguese (Brazilian),
PT-"PT" : Portuguese (all Portuguese varieties excluding Brazilian Portuguese),
"RO" : Romanian,
"RU" : Russian,
"SK" : Slovak,
"SL" : Slovenian,
"SV" : Swedish,
"TR" : Turkish,
"UK" : Ukrainian,
"ZH" : Chinese (simplified),
}
"""

def translate(code, target):
    """
    text1_sent = sent_tokenize(text1)[0]

    goog = str(google_trans.detect(text1_sent).lang).upper()
    if goog == 'EN': #here since some language have different versions like english and british english we had to make sure that is always US english
        goog = goog + '-US'
    if goog == 'PT': #same goes for portuguese 
        goog = goog + '-BR'
    # goog is the name of the language that we are changing right box into
    goog = 'EN-US'
    """   
    if (code == "en"):
        code = "en-us"
    if (code == "pt"):
        code = "pt-br" 
    code = code.upper()

    if len(target) < 4500:
        for language in deeplLangs:
            if code == language:
                result = deepl_trans.translate_text(target, target_lang = language) #turns target into the translated language we want
                return result

    else:
        result = ""
        iterations = math.ceil(len(target)/4450)
        i = 0
        for language in deeplLangs:
            if code == language:
                textFragments = wrap(target, 4450, break_long_words=False) #first 4450 to translate without breaking words
                while i < iterations:
                    resultFragment = ""
                    resultFragment = deepl_trans.translate_text(textFragments[i], target_lang = language) 
                    result = result + str(resultFragment)
                    i += 1
        return result
    #if this line is hit, return the popup that user will have to manually translate
