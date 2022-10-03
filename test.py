# REF: README.md
# For individual sentences
from nltk.translate.bleu_score import sentence_bleu
# For whole paragraphs/texts
from nltk.translate.bleu_score import corpus_bleu

# REF: https://www.nltk.org/api/nltk.translate.bleu_score.html

# Sentence translated from another language (eg: A sentence translated from French to English)
hypothesis = "".split()
# Original translation (eg: A sentence in English)
reference = "".split()

'''
REF: https://cloud.google.com/translate/automl/docs/evaluate
< .1 - Almost useless
[.1, .19] - Hard to get the gist
[.2 - .29] - The gist is clear, but has significant grammatical errors
[.3 - .4] - Understandable to good translations
[.4 - .5] - High quality translations
[.5 - .6] - Very high quality, adequate, and fluent translations
> .6 - Quality often better than human
'''
# Comparison between sentences

# We split because sentence_bleu reads an array of strings (individual words)



print("Test 2")
# Sentence translated from another language (eg: A sentence translated from French to English)
hypothesis = "I can't believe that people actually consider deep dish pizza real pizza, it's more of a casserole to me.".split()
# Original translation (eg: A sentence in English)
reference = "I can't believe people actually consider deep pizza to be real pizza, it's more of a pan.".split()


score = sentence_bleu([reference], hypothesis)
# Display result of comparison 
print("BLEU Score:", score)