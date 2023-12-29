import spacy
#from spacypdfreader import pdf_reader
from spacy.matcher import PhraseMatcher
from pdfminer.high_level import extract_text
from spacy.tokens import Span

nlp = spacy.load("en_core_web_lg")

text = extract_text("2022146248.pdf")
#print(text)

doc = nlp(text)

matcher = PhraseMatcher(nlp.vocab)

pattern = nlp("GRANTOR")

matcher.add("SELLER", [pattern])

for match_id, start, end in matcher(doc):
    span = doc[start:(end+50)]
    #print(span)

    buyer = ""
    seller = ""

    for ent in span.ents:
        if ent.label_ == "ORG" and seller == "":
            seller += ent.text
        if ent.label_ == "PERSON" and seller != "":
            buyer += ent.text

    print("Buyer : {} --- Seller : {}".format(buyer, seller))
            #print("Text : {}\nType : {}\n".format(ent.text, ent.label_))







#for ent in doc2.ents:
    #if ent.label_ == "PERSON":
        #print("Text : {}\nType : {}\n".format(ent.text, ent.label_))
        #if "sell" in ent.text.lower():
            #print("Seller:", ent.text)



''' pdf reader code
doc = pdf_reader("2022-00011389.pdf", nlp)

max_page = doc._.last_page
for i in range(1, max_page):
    print("Page No {}:".format(i))
    print(doc._.page(i))

#for ent in doc.ents:
    #print("Text : {}\nType : {}\n".format(ent.text, ent.label_))
'''





'''
matcher = Matcher(nlp.vocab)

pattern = [{"TEXT": "payment"}, {"TEXT": "of"}]
matcher.add("PAYMENT_PATTERN", [pattern])

matches = matcher(doc)
print(matches)

for match_id, start, end in matches:
    matched_span = doc[start:end]
    print(matched_span.text)'''