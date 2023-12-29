import fitz
import spacy
from pathlib import Path

out_directory = Path(r"C:\Users\e408590\Desktop\project\pdf scripts\Outputs").expanduser()
text_file = out_directory / Path("fitzOP.txt")

nlp = spacy.load("en_core_web_lg")
with fitz.open("202100006723.pdf") as docu:
    text = ""
    for page_num in range(docu.page_count):
        page = docu.load_page(page_num)
        text += page.get_text("text")


with open(text_file, "a") as output_file:
    output_file.write(text)

#print(text)
'''
doc = nlp(text)

for ind, ent in enumerate(doc.ents):
    print("{}. Text : {}\nType : {}\n".format(ind+1, ent.text, ent.label_))'''
