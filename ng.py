import nltk
nltk.download('punkt_tab')
from nltk.util import ngrams
from nltk.tokenize import word_tokenize
sentence = "natural language processing is very interesting"
tokens = word_tokenize(sentence)
unigrams = list(ngrams(tokens,1))
bigrams = list(ngrams(tokens,2))
trigrams = list(ngrams(tokens,3))
print("Input Sentence :",sentence)
print("\nUnigrams :")
print(unigrams)
print("\nBigrams :")
print(bigrams)
print("\nTrigrams :")
print(trigrams)