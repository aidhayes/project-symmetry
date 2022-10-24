import tensorflow_hub as hub
  
# Load pre-trained universal sentence encoder model
embed = hub.load("https://tfhub.dev/google/universal-sentence-encoder/4")
  
# Sentences for which you want to create embeddings,
# passed as an array in embed()
Sentences = [
    "How old are you",
    "What is your age",
    "I love to watch Television",
    "I am wearing a wrist watch"
]
embeddings = embed(Sentences)
  
# Printing embeddings of each sentence
print(embeddings)
  
# To print each embeddings along with its corresponding 
# sentence below code can be used.
for i in range(len(Sentences)):
    print(Sentences[i])
    print(embeddings[i])