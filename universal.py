import tensorflow as tf
import tensorflow_hub as hub
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


def similarity_array(paragraph1:list, paragraph2:list):
  return cosine_similarity(model(paragraph1),model(paragraph2))

def dict_output(paragraph1: list, paragraph2: list, sim_array: np.ndarray, sim_r: float):
  dict1 = dict.fromkeys(paragraph1)
  dict2 = dict.fromkeys(paragraph2)
  cur_num = 1
  for i1, s1 in enumerate(dict1):
    for i2, s2 in enumerate(dict2):
      if sim_array[i1][i2] >= sim_r:
        if dict1[s1] is None and dict2[s2] is None:
          dict1[s1] = cur_num
          dict2[s2] = cur_num
          cur_num = cur_num + 1
        elif dict1[s1] is None:
          dict1[s1] = dict2[s2]
        elif dict2[s2] is None:
          dict2[s2] = dict1[s1]
  return dict1, dict2

