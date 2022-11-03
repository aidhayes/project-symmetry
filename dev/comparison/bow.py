import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from nltk.tokenize import sent_tokenize

def bagofwords(article1, article2):
    list1 = sent_tokenize(article1)
    list2 = sent_tokenize(article2)

    for sent1 in list1:
        for sent2 in list2:
            CountVec = CountVectorizer(ngram_range=(1,1), stop_words='english')
            Count_data = CountVec.fit_transform([sent1, sent2])
            cv_dataframe=pd.DataFrame(Count_data.toarray(), columns=CountVec.get_feature_names())
            print(cv_dataframe)



article1 = "I like milk. Milk is good. I like cheese."
article2 = "I like milk. I am god. Milk is good."

bagofwords(article1, article2)


