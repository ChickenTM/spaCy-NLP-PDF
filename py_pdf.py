from PyPDF2 import PdfReader
import spacy

nlp = spacy.load("en_core_web_lg")
# Open the PDF file and create a PDF reader object
# pdf_file = open("deed1.pdf", "rb")
pdf_reader = PdfReader("deed1.pdf")

# Extract text from all pages of the PDF file
text = ""
for page_num in range(len(pdf_reader.pages)):
    page = pdf_reader.pages[page_num]
    text += page.extract_text()


doc = nlp(text)

for ind, ent in enumerate(doc.ents):
    print("{}. Text : {}\nType : {}\n".format(ind+1, ent.text, ent.label_))