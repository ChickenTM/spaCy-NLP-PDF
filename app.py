import spacy
#from spacy import load

nlp = spacy.load("en_core_web_sm")

doc = nlp("Apple is a technology company based in Cupertino, California.")

#with open("sampledata.txt", "r") as f:
    #text = f.read()

#doc = nlp(text)

for ent in doc.ents:
    print("Text : {}\nType : {}\n".format(ent.text, ent.label_))