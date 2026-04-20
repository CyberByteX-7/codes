import nltk
from nltk.tokenize import word_tokenize
nltk.download('punkt_tab')
text="this is an example of word tokenization"
Tokens=word_tokenize(text)
print(Tokens)