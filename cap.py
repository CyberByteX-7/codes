import nltk
from nltk.tokenize import word_tokenize
from nltk import pos_tag
nltk.download('punkt_tab')
nltk.download('averaged_perceptron_tagger_eng')
text= input("Enter a Sentence :")
words = word_tokenize(text)
tagged_words= pos_tag(words)
connectors = []
prepositions = []
for word, tag in tagged_words:
  if tag == 'CC':
    connectors.append(word)
  elif tag == 'IN':
    prepositions.append(word)
print("\nTagged words :")
print(tagged_words)
print("\nconnectors (Conjunctions):")
print(connectors)
print("\nPrepositions:")
print(prepositions)