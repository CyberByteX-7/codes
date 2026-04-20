import nltk
import random
from nltk.util import ngrams
from collections import Counter, defaultdict
nltk.download('punkt_tab')
nltk.download('averaged_perceptron_tagger_eng')
nltk.download('gutenberg')
from nltk.corpus import gutenberg
text = gutenberg.raw('austen-emma.txt')
tokens = nltk.word_tokenize(text)
tokens = [w.lower() for w in tokens if w.isalpha()]
print("Total words:",len(tokens))
freq = Counter(tokens)
print("\nTop 10 words:")
for word, count in freq.most_common(10):
  print(word, count)