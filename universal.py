import tensorflow as tf
import tensorflow_hub as hub
import tensorflow_text
from sklearn.metrics.pairwise import cosine_similarity
import nltk
import ssl

try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context

try:
  nltk.data.find('tokenizers/punkt')
except LookupError:
  nltk.download('punkt')
from nltk.tokenize import sent_tokenize
model_url = "https://tfhub.dev/google/universal-sentence-encoder-multilingual-large/3"
model = hub.load(model_url)
import numpy as np

dict1 = dict()
dict2 = dict()

def similarity_array(paragraph1:list, paragraph2:list):
  return cosine_similarity(model(paragraph1),model(paragraph2))

def dict_output(paragraph1, paragraph2, sim_array, sim = .5):
  list1 = sent_tokenize(paragraph1)
  list2 = sent_tokenize(paragraph2)
  for i1, s1 in enumerate(list1):
    for i2, s2 in enumerate(list2):
      if sim_array[i1][i2] >= sim:
        if list1 not in dict1:
                    '''
                    key = reference
                    value = hypothesis
                    eg:
                        key = English sentence
                        value = French sentence translated to English
                    '''
                    dict1[list1] = list2
                    
                    '''
                    key = hypothesis
                    value = reference
                    eg:
                        key = French sentence translated to English
                        value = English sentence
                    '''
                    dict2[list2] = list1
        
    return dict1, dict2



par1 = "Today is a great day to go for a walk. The sun is out with no clouds and no humidity. Maybe after my walk I will go get some lunch. My favorite thing to eat for lunch is a italian sub. Then later I will go out with my friends and go see a movie. I heard the new Marvel moive is amazing and a must see."
par2 = "Today is an amazing day to go for a run. The sun is out with a little bit of clouds and no humidity. Maybe after my run I will go get some lunch. My favorite thing to eat for lunch is and italian sub. Then later I think I will go out with my friends and go see a movie. I heard the new DC movie is pretty good anf a must see."

dict1, dict2 = dict_output(par1, par2)
print(dict1)
print(dict2)
