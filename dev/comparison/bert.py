#Example code from https://www.sbert.net/docs/quickstart.html
#To import use the command pip install -U sentence-transformers
#Import the for the Bert model
from sentence_transformers import SentenceTransformer, util
from sentence_transformers import SentenceTransformer, util
from nltk.tokenize import sent_tokenize

#SentenceTransformer takes a type of model name that is provide on the the website https://www.sbert.net/docs/pretrained_models.html.
#'all-MiniLM-L6-v2' is the model with the highest performace number of 69.57%,
#compare to the 'multi-qa-mpnet-base-dot-v1  which has a 66.76% is the second best one.'
model = SentenceTransformer('all-MiniLM-L6-v2')

def compare(par1, par2, colors, similarity=.5):
    list1 = sent_tokenize(par1)
    list2 = sent_tokenize(par2)
    dict1 = dict()
    dict2 = dict()

    cos_sim = util.cos_sim(model.encode(list1), model.encode(list2))

    for i in range(len(list1)):
        for j in range(len(list2)):
            if cos_sim[i][j] >= similarity:
                if list1[i] not in dict1 and list2[j] not in dict2:
                    dict1[list1[i]] = [list2[j], colors[i]]
                    dict2[list2[j]] = [list1[i], colors[i]]

    return dict1, dict2