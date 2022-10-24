import tensorflow as tf
import tensorflow_hub as hub
import tensorflow_text
from sklearn.metrics.pairwise import cosine_similarity
import nltk
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

def dict_output(paragraph1, paragraph2, sim_array, sim):
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

