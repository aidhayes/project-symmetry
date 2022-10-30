#Example code from https://www.sbert.net/docs/quickstart.html
#To import use the command pip install -U sentence-transformers
#Import the for the Bert model
from sentence_transformers import SentenceTransformer, util
import colors
from sentence_transformers import SentenceTransformer, util
from nltk.tokenize import sent_tokenize

#SentenceTransformer takes a type of model name that is provide on the the website https://www.sbert.net/docs/pretrained_models.html.
#'all-MiniLM-L6-v2' is the model with the highest performace number of 69.57%,
#compare to the 'multi-qa-mpnet-base-dot-v1  which has a 66.76% is the second best one.'
model = SentenceTransformer('all-MiniLM-L6-v2')


#Sentences that we are testing
sentences = [
          'Rome, all while attracting a large following of imitators and students. Upon the invitation of Francis I,'
          ' he spent his last three years in France, where he died in 1519.',
          'Rome, all whereas pulling in a huge taking after of imitators and understudies. Upon the welcome of Francis I,' 
          ' he went through his final three a long time in France, where he kicked the bucket in 1519.',
          'A man is riding a horse.',
          'A woman is playing violin.',
          'Two men pushed carts through the woods.',
          'A man is riding a white horse on an enclosed ground.',
          'A monkey is playing drums.',
          'Someone in a gorilla costume is playing a set of drums.'
          ]

#Encode all sentences
embeddings = model.encode(sentences)

#Compute cosine similarity between all pairs
cos_sim = util.cos_sim(embeddings, embeddings)

#Add all pairs to a list with their cosine similarity score
all_sentence_combinations = []
for i in range(len(cos_sim)-1):
    for j in range(i+1, len(cos_sim)):
        all_sentence_combinations.append([cos_sim[i][j], i, j])

#Sort list by the highest cosine similarity score
all_sentence_combinations = sorted(all_sentence_combinations, key=lambda x: x[0], reverse=True)

print("Top-5 most similar pairs:")
for score, i, j in all_sentence_combinations[0:5]:
    print("{} \t {} \t {:.4f}".format(sentences[i], sentences[j], cos_sim[i][j]))