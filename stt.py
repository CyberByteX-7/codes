import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
nltk.download('punkt_tab')
text ="The studenta were studying various subjects while playing games"
text = text.lower()
tokens = word_tokenize(text)
print("Tokens")
print(tokens)
ps = PorterStemmer()
print("\nStemming Output :")
for word in tokens:
  print(word, "->", ps.stem(word))