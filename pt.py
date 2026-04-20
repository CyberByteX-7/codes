text="lambo is good.it is hyper or sport! do you know? yes,its an sport."
text=text.replace("?",".").replace("!",".")
sentence=text.split(".")
sentence=[sentence.strip() for sentence in sentence if sentence.strip() !=""]
print("sentence:")
for i,sentence in enumerate(sentence,start=1):
  print(f"{i}.{sentence}")