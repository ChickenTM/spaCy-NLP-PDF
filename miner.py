import spacy
from pdfminer.high_level import extract_text
from spacy.matcher import Matcher
from spacy.tokens import Token

pattern = [{"IS_ASCII": True, "LOWER":{"REGEX": r"(?<![a-z0-9])[g][a-z0-9]*[r](?=\W|$)" }}]

Token.set_extension("matched_words", default=[], force=True)

nlp = spacy.load("en_core_web_lg")

matcher = Matcher(nlp.vocab)
matcher.add("pattern", [pattern])

#text = extract_text("testpdf.pdf", page_numbers=[0])

with open("samplefile.txt", "r") as f:
    text = f.read()

doc = nlp(text)

matches = matcher(doc)

#for ind, ent in enumerate(doc.ents):
    #print("{}. Text : {}\nType : {}\n".format(ind+1, ent.text, ent.label_))

#buyer = ""
#seller = ""

buyer_flag = 0
Seller_flag = 0


for match_id, start, end in matches:
    for token in doc[start:end]:
        token._.matched_words.append(token.text)

    if token._.matched_words:
        print("matched word:", token._.matched_words)
        span = doc[start:(end+50)]
        print("Span : ", span)
        
        seller = ""
        
        for ent in span.ents:
            if seller == "" and ((ent.label_ == "PERSON" or ent.label_ == "ORG") and (ent.text.lower() != "grantor" and ent.text.lower() != "grantee" )):
                #print("entity ----", ent)
                #print("text : {}, label : {}".format(ent.text, ent.label_))
                for token in doc[ent.start:]:
                    print(token.text, token.pos_)
                    if token.pos_ == "NOUN" or token.pos_ == "PROPN" or token.pos_ == "PUNCT":
                        seller += token.text + " "
                    else:
                        break
            #elif seller != "" and    
            
    
                



'''if (ent.label_ == "PERSON" or ent.label_ =="ORG") and (ent.text.lower() != "grantor" and ent.text.lower() != "grantee" ):
                start_index = ent.start
                

                for token in doc[start_index:]:
                    print(token.text)
                    if token.pos_ != "NOUN" and token.pos_ != "PROPN":
                        break
                    else:
                        seller += token.text + " "

                    

                seller = seller.strip()'''
                

                
            
            
            #if ent.label_ == "PERSON" and seller != "" and (ent.text.lower() != "grantor" and ent.text.lower() != "grantee" ) and (ent.text.lower() not in seller.lower()):
                #buyer += ent.text

            

#print("Buyer : {} --- Seller : {}".format(buyer, seller))


'''
for token in doc:
    if token._.matched_words:
        print("Output : ", token._.matched_words)'''


#for ind, ent in enumerate(doc.ents):
    #print("{}. Text : {}\nType : {}\n".format(ind+1, ent.text, ent.label_))



#for token in doc:
    #print(token.text)
''' ------ print each entity-------
for ind, ent in enumerate(doc.ents):
    print("{}. Text : {}\nType : {}\n".format(ind+1, ent.text, ent.label_))'''


