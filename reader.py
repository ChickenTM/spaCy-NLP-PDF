import spacy
from spacypdfreader import pdf_reader
from spacy.matcher import Matcher
from spacy.tokens import Token

pattern = [{"IS_ASCII": True, "LOWER":{"REGEX": r"(?<![a-z0-9])[g][a-z0-9]*[r](?=\W|$)" }}]

Token.set_extension("matched_words", default=[], force=True)

nlp = spacy.load("en_core_web_lg")

matcher = Matcher(nlp.vocab)
matcher.add("pattern", [pattern])

text = pdf_reader("deed2.pdf", nlp)
doc = text._.page(text._.first_page)

matches = matcher(doc)

for match_id, start, end in matches:
    for token in doc[start:end]:
        token._.matched_words.append(token.text)

    if token._.matched_words:
        print("matched word:", token._.matched_words)
        span = doc[start:(end+30)]
        print("Span : ", span)
        buyer = ""
        seller = ""
        
        for ent in span.ents:
            if((ent.label_ == "PERSON" or ent.label_ == "ORG") and (ent.text.lower() != "grantor" and ent.text.lower() != "grantee" )):
                print("entity ----", ent)
                print("text : {}, label : {}".format(ent.text, ent.label_))
                for token in doc[ent.start:]:
                    #print(token.text, token.pos_)
                    if token.pos_ == "NOUN" or token.pos_ == "PROPN" or token.pos_ == "PUNCT":
                        seller += token.text + " "
                        #print("seller : ", seller)
                    else:
                        break


#for ind, ent in enumerate(doc.ents):
#    if(ent.label_ == "PERSON" or ent.label_ == "ORG"):
#        print("{}. Text : {}\nType : {}\n".format(ind+1, ent.text, ent.label_))