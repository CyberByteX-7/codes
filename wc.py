from urllib.request import urlopen
import re
url = "https://www.gutenberg.org/files/84/84-0.txt"
response = urlopen(url)
text = response.read().decode('utf-8')
text = text.lower()
words = re.findall(r'\b[a-z]+\b',text)
corpus = words
print("Total words in corpus :",len(corpus))
print("First 20 words :")
print(corpus[:20])