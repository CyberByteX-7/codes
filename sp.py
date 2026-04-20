import nltk
from nltk import CFG, ChartParser
grammar = CFG.fromstring("""
S -> NP VP
NP -> DT N | Pronoun | ProperNoun
VP -> V NP | V
DT -> 'a' | 'the'
N -> 'man' | 'dog' | 'cat'
Pronoun -> 'I' | 'he' | 'she'
ProperNoun -> 'Man' | 'Mary'
V -> 'saw' | 'likes' | 'walked'
""")
parser = ChartParser(grammar)
sentence = "Man saw a dog".split()
print(f"Parsing sentence: {' '.join(sentence)}")
for tree in parser.parse(sentence):
    print(tree)
    tree.pretty_print()