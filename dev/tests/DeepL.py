#The required imports needed ,pip install --upgrade deepl
import deepl

#This api code was found in the google drive under the Final T5 and MariranNMT.ipymb 
auth_key = "0ff6b0ef-fc20-631e-6feb-695b9d666743:fx" 
translator = deepl.Translator(auth_key)


text = input("Enter senetence to be translated!\n")

#List of languages can be founded on https://www.deepl.com/docs-api/translate-text/ 
user_language = input("Enter the target language you want.(BG CS DA DE FL EN ES ET FI FR HU ID IT JA LT)\n"
    "LV NL PL PT RO RU SK SL SV TR UK ZH\n")


result = translator.translate_text(text, target_lang= user_language )
#Prints the results 
print(result.text)  

