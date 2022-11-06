# REF: README.md
# For individual sentences
from nltk.translate.bleu_score import sentence_bleu
# For whole paragraphs/texts
from nltk.translate.bleu_score import corpus_bleu

# REF: https://www.nltk.org/api/nltk.translate.bleu_score.html

# Sentence translated from another language (eg: A sentence translated from French to English)
hypothesis = "I like to eat Buffalo Chicken Wings on Sundays while I watch football.".split()
# Original translation (eg: A sentence in English)
reference = "I like eating buffalo chicken wings on Sundays while I watch football.".split()
# We split because sentence_bleu reads an array of strings (individual words)


'''
REF: https://cloud.google.com/translate/automl/docs/evaluate
< .1 - Almost useless
[.1, .19] - Hard to get the gist
[.2 - .29] - The gist is clear, but has significant grammatical errors
[.3 - .39] - Understandable to good translations
[.4 - .49] - High quality translations
[.5 - .59] - Very high quality, adequate, and fluent translations
>= .6 - Quality often better than human
'''

# Comparison between sentences
score = sentence_bleu([reference], hypothesis)

# Display result of comparison 
print(score) 