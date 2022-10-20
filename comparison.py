# REF: README.md
# For individual sentences
from nltk.translate.bleu_score import sentence_bleu
# For whole paragraphs/texts
from nltk.translate.bleu_score import corpus_bleu
from nltk.tokenize import sent_tokenize
from nltk.translate.bleu_score import SmoothingFunction

'''
Compare 2 Wikipedia articles to find sentences present in one but not the other
'''
def compare(ref, hypothesis, similarity=0.1):
    # Tokenize paragraphs so they can be traversed as an array
    ref_list = sent_tokenize(ref)
    hyp_list = sent_tokenize(hypothesis)

    no_pairs = []
    pairs = []

    # Itteration over both paragraphs
    for ref in ref_list:
        for hyp in hyp_list:
            #Determine if the current sentence has a match or not
            if sentence_bleu([ref.split()], hyp.split(), smoothing_function=SmoothingFunction().method7) >= similarity:
                # Check for duplicates
                if ref not in pairs:
                    pairs.append(ref)
                # Check to see if sentence was determined to have no pair in previous itteration
                if ref in no_pairs:
                    no_pairs.remove(ref)   
            else:
                # If the setence hasn't been added to either array yet
                if ref not in no_pairs and ref not in pairs:
                    no_pairs.append(ref)

    return [pairs, no_pairs]
