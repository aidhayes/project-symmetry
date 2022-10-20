# REF: README.md
# For individual sentences
from nltk.translate.bleu_score import sentence_bleu
# For whole paragraphs/texts
from nltk.translate.bleu_score import corpus_bleu
from nltk.tokenize import sent_tokenize
from nltk.translate.bleu_score import SmoothingFunction
import colorama
from colorama import init, Fore
import sys


'''
Compare 2 Wikipedia articles to find sentences present in one but not the other
'''
def compare(ref, hypothesis, similarity=0.1):
    # Tokenize paragraphs so they can be traversed as an array
    ref_list = sent_tokenize(ref)
    hyp_list = sent_tokenize(hypothesis)

    no_pairs = []
    pairs = []

    pair_dict = dict()
    # Itteration over both paragraphs

    init(convert=True)

    for i in range(len(ref_list)):
        for j in range(len(hyp_list)):
            if sentence_bleu([ref_list[i].split()], hyp_list[j].split(), smoothing_function=SmoothingFunction().method7) >= similarity:
                if ref_list[i] not in pair_dict:
                    ref_list[i] = Fore.RED + ref_list[i]
                    hyp_list[j] = Fore.RED + hyp_list[j]
                    pair_dict[ref_list[i]] = hyp_list[j]
                # Check to see if sentence was determined to have no pair in previous itteration
                if ref_list[i] in no_pairs:
                    no_pairs.remove(ref_list[i])   
            else:
                # If the setence hasn't been added to either array yet
                if ref_list[i] not in no_pairs and ref_list[i] not in pairs:
                    no_pairs.append(ref_list[i])


    '''
        for ref in ref_list:
            for hyp in hyp_list:
                #Determine if the current sentence has a match or not
                if sentence_bleu([ref.split()], hyp.split(), smoothing_function=SmoothingFunction().method7) >= similarity:
                    # Check for duplicates
                    if ref not in pair_dict:
                        # pairs.append(ref)
                        ref = Fore.RED + ref
                        hyp = Fore.RED + hyp
                        pair_dict[ref] = hyp
                    # Check to see if sentence was determined to have no pair in previous itteration
                    if ref in no_pairs:
                        no_pairs.remove(ref)   
                else:
                    # If the setence hasn't been added to either array yet
                    if ref not in no_pairs and ref not in pairs:
                        no_pairs.append(ref)
    '''
    return [" ".join(ref_list), " ".join(hyp_list)]
