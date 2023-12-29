import spacy
import pdfplumber

with pdfplumber.open("deed3.pdf") as pdf:
    page = pdf.pages[0]
    text = page.extract_text()

nlp = spacy.load("en_core_web_lg")

doc = nlp(text)


columns = []
for line in doc.sents:
    for i, token in enumerate(line):
        if i >= len(columns):
            columns.append([])
        columns[i].append(token.text)

for col in columns:
    print(" ".join(col))


#for ind, ent in enumerate(doc.ents):
#    print("{}. Text : {}\nType : {}\n".format(ind+1, ent.text, ent.label_))