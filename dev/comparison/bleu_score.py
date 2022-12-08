# REF: README.md
# For individual sentences
from nltk.translate.bleu_score import sentence_bleu
# For whole paragraphs/texts
from nltk.translate.bleu_score import corpus_bleu
from nltk.tokenize import sent_tokenize
from nltk.translate.bleu_score import SmoothingFunction
import time

'''
Compare 2 Wikipedia articles to find sentences present in one but not the other
'''
def compare(ref, hypothesis, colors, similarity=0.1):
    # Tokenize paragraphs so they can be traversed as an array
    ref_list = sent_tokenize(ref)
    # print("Ref length: ", len(ref_list))
    hyp_list = sent_tokenize(hypothesis)
    # print("Hyp length: ", len(hyp_list))
    i = 0
    ref_pair_dict = dict()
    hyp_pair_dict = dict()
    # Iteration over both paragraphs
    start_time_1 = time.time()
    for ref in ref_list:
        for hyp in hyp_list:
            # Determine if the current sentence has a match or not
            start_time = time.time()
            bleu_score = sentence_bleu([ref.split()], hyp.split(), smoothing_function=SmoothingFunction().method7)
            if bleu_score >= similarity:
                # Check for duplicates
                i += 1

                if (ref not in ref_pair_dict and hyp not in hyp_pair_dict):
                    '''
                    key = reference
                    value = hypothesis
                    eg:
                        key = English sentence
                        value = French sentence translated to English
                    '''
                    ref_pair_dict[ref] = [hyp, colors[i]]
                    
                    '''
                    key = hypothesis
                    value = reference
                    eg:
                        key = French sentence translated to English
                        value = English sentence
                    '''
                    hyp_pair_dict[hyp] = [ref, colors[i]]
                '''
                else:
                    if ref in ref_pair_dict:
                        if bleu_score > sentence_bleu([ref.split()], ref_pair_dict[ref][0].split(), smoothing_function=SmoothingFunction().method7):
                            ref_pair_dict[ref] = [hyp, colors[i]]
                            hyp_pair_dict[hyp] = [ref, colors[i]]
                '''

        #print(hyp_pair_dict)
        #print(ref_pair_dict)
                    # print(f"Iteration Time:  {end_time - start_time}")
    end_time_1 = time.time()
    print(f"Iteration Time:  {end_time_1 - start_time_1}")
    return ref_pair_dict, hyp_pair_dict
