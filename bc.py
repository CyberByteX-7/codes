import nltk
sentence = "The quick brown fox jumps over the lazy dog"
tokens = nltk.word_tokenize(sentence)
pos_tags = nltk.pos_tag(tokens)
grammar = r"""
  NP: {<DT>?<JJ>*<NN>}
  VP: {<VB.*><NP|PP>*}
  PP: {<IN><NP>}
"""
chunk_parser = nltk.RegexpParser(grammar)
result = chunk_parser.parse(pos_tags)
print("Tokens:", tokens)
print("POS Tags:", pos_tags)
print("Chunk Tree:", result)