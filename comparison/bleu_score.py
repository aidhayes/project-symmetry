# REF: README.md
# For individual sentences
from nltk.translate.bleu_score import sentence_bleu
# For whole paragraphs/texts
from nltk.translate.bleu_score import corpus_bleu
from nltk.tokenize import sent_tokenize
from nltk.translate.bleu_score import SmoothingFunction
import ui.colors as colors


'''
Compare 2 Wikipedia articles to find sentences present in one but not the other
'''
def compare(ref, hypothesis, similarity=0.1):
    # Tokenize paragraphs so they can be traversed as an array
    ref_list = sent_tokenize(ref)
    hyp_list = sent_tokenize(hypothesis)
    i = 0
    ref_pair_dict = dict()
    hyp_pair_dict = dict()
    # Itteration over both paragraphs
    for ref in ref_list:
        for hyp in hyp_list:
            # Determine if the current sentence has a match or not
            if sentence_bleu([ref.split()], hyp.split(), smoothing_function=SmoothingFunction().method7) >= similarity:
                # Check for duplicates
                if ref not in ref_pair_dict and hyp not in hyp_pair_dict:
                    highlight = colors.gen_color()
                    '''
                    key = reference
                    value = hypothesis
                    eg:
                        key = English sentence
                        value = French sentence translated to English
                    '''
                    ref_pair_dict[ref] = [hyp, highlight]
                    
                    '''
                    key = hypothesis
                    value = reference
                    eg:
                        key = French sentence translated to English
                        value = English sentence
                    '''
                    hyp_pair_dict[hyp] = [ref, highlight]

        print(hyp_pair_dict)
        print(ref_pair_dict)
    return ref_pair_dict, hyp_pair_dict
