import spacy
from spacy.matcher import Matcher

nlp = spacy.load("en_core_web_sm")

doc = nlp("I am Ironman")

lexeme = nlp.vocab["Ironman"]
print(lexeme.text, lexeme.orth, lexeme.is_alpha)

#print("Hash value:", nlp.vocab.strings["Ironman"])
#print("String Value:", nlp.vocab.strings[15388312735200753304])

'''---------matcher code----------

matcher = Matcher(nlp.vocab)

pattern = [{"TEXT": "iPhone"}, {"TEXT": "X"}]
matcher.add("IPHONE_PATTERN", [pattern])

doc = nlp("Upcoming iPhone X release date leaked")

matches = matcher(doc)

for match_id, start, end in matches:
    matched_span = doc[start:end]
    print(matched_span.text)
'''
#doc = nlp("The girl sitting on the wall ate all the icecream")
#doc = nlp("Apple is a technology company based in Cupertino, California.")
#doc = nlp("Apple is looking at buying U.K. startup for ₹123,457,789")

#for ent in doc.ents:
    #print(ent.text, ent.label_)
#for token in doc:
 #   print(token.text, token.pos_)