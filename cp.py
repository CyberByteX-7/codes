import nltk
sentence = "The is a loving subject"
tokens = nltk.word_tokenize(sentence)
pos_tags = nltk.pos_tag(tokens)
print("Tokens : ",tokens)
print("Pos Tag :",pos_tags)
grammar = r"""
  NP: {<DT|JJ|NN.*>+}          
  PP: {<IN><NP>}               
  VP: {<VB.*><NP|PP>*}         
"""
chunk_parser = nltk.RegexpParser(grammar)
result = chunk_parser.parse(pos_tags)
print("Tree Structure :",result)