import spacy
from pdfminer.high_level import extract_text

nlp = spacy.load("en_core_web_lg")

text = extract_text("testpdf.pdf")

doc = nlp(text)

for ind, ent in enumerate(doc.ents):
    print("{}. Text : {}\nType : {}\n".format(ind+1, ent.text, ent.label_))

#for ind, token in enumerate(doc):
    #print("{}. Text : {}\n POS : {}\n".format(ind+1, token.text, token.pos_))
