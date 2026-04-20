import nltk
from nltk.tokenize import sent_tokenize
text = "This is an example of sentence tokenization. It can split a paragraph into individual sentences."
sentences = sent_tokenize(text)
print(sentences)