from docx import *
import re

def FindText():
    document = Document(r"C:\Users\1\Desktop\Test.docx")
    full_text = []
    for para in document.paragraphs:
        full_text.append(para.text)
        print(full_text)
    for str_num, string in enumerate(full_text):
        pos_found = [pos.start() for pos in re.finditer(r'is\b', string)]
        return ("The string: {} was found in the sentense {} on position(s): ".format("is", str_num)
                + " ".join("{}" for _ in range(len(pos_found))).format(*pos_found))

print(FindText())
