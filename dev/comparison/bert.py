# To import use the command pip install -U sentence-transformers
# Import the for the Bert model
from sentence_transformers import SentenceTransformer, util
from sentence_transformers import SentenceTransformer, util
from nltk.tokenize import sent_tokenize

'''
SentenceTransformer takes a type of model name that is provide on the the website https://www.sbert.net/docs/pretrained_models.html.
'all-MiniLM-L6-v2' is the model with the highest performace number of 69.57%,
compare to the 'multi-qa-mpnet-base-dot-v1  which has a 66.76% is the second best one.'
'''
model = SentenceTransformer('all-MiniLM-L6-v2')

'''
Iterates over the source and the target articles sentence by sentence and 
uses Sentence Bert to determine whether two sentences have a similarity score
GREATER OR EQUAL to the chosen similarity score.

For more information on Sentence Bert, visit: https://www.sbert.net

param:
    source: Article in a users native language
    target: Same article as source but in another language
    colors: randomly generated list of colors for highlighting
    similarity: similarity score that will be used to determine matching sentences

return:
    dictionaries of the form:
        {
            "sentence": ["matching sentence", "highlight color"],
            ...
        }
    source_pair_dict:   dictionary with sentences from source as key and value as a list containing matching sentences
                        from target and color to be highlighted
    target_pair_dict:   dictionary with sentences from target as key and value as a list containing matching sentences
                        from source and color to be highlighted

Contributors:
Raj Jagroup, Yulong Chen
'''
def compare(source, target, colors, similarity=.5):
    # Tokenize paragraphs so they can be traversed as an array
    source_list = sent_tokenize(source)
    target_list = sent_tokenize(target)

    # Intialize dictionaries
    source_pairs = dict()
    target_pairs = dict()

    # Generate cosine similarity array between the source and target articles
    cos_sim = util.cos_sim(model.encode(source_list), model.encode(target_list))

    # Iteration over both articles
    for i in range(len(source_list)):
        for j in range(len(target_list)):
            # If the cosine similarity of the two sentences is GREATER THAN OR EQUAL TO the desired similarity score
            if cos_sim[i][j] >= similarity:
                # Check for duplicates
                if source_list[i] not in source_pairs and target_list[j] not in target_pairs:
                    source_pairs[source_list[i]] = [target_list[j], colors[i]]
                    target_pairs[target_list[j]] = [source_list[i], colors[i]]

    return source_pairs, target_pairs