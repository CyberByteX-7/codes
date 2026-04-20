import nltk
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger_eng')
sentence = "The dog chased the cat"
tokens = nltk.word_tokenize(sentence)
pos_tags = nltk.pos_tag(tokens)
print("Tokens:", tokens)
print("POS Tags:", pos_tags)