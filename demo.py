import spacy
from spacy.tokens import Doc, Span

nlp = spacy.load("en_core_web_sm")


words = ["Hello", "World", "!", "Apple", "Inc", "is", "in", "California"]
spaces = [True, False, True, True, True, True, True, False]

doc = Doc(nlp.vocab, words = words, spaces = spaces)

span = Span(doc, 0, 2)

span_with_label = Span(doc, 0, 2, label="Greeting")

doc.ents = [span_with_label]

for ent in doc.ents:
    print("Text : {}\nType : {}\n".format(ent.text, ent.label_))