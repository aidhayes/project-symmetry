#REF: README.md
#For individual sentences
from nltk.translate.bleu_score import sentence_bleu
#For whole paragraphs/texts
from nltk.translate.bleu_score import corpus_bleu

#REF: https://www.nltk.org/api/nltk.translate.bleu_score.html

#Sentence translated from another language (eg: A sentence translated from French to English)
hypothesis = "".split()
#Original translation (eg: A sentence in English)
reference = "".split()

#We split because sentence_bleu reads an array of strings (individual words)
