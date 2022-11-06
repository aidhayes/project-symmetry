import fasttext as ft
import deepl

auth_key = "0ff6b0ef-fc20-631e-6feb-695b9d666743:fx" 
translator = deepl.Translator(auth_key)

# Load the pretrained model
ft_model = ft.load_model("./pretrained_model/lid.176.bin")

def translate (text, text2, model = ft_model):

  text = text.replace('\n', " ")
  prediction = model.predict([text])


  # detect langauge of text1
  # translate text2 to language of text1
  # return text2
  text2 = translator.translate_text(text, prediction)

  return text2 

