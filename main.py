import pyttsx3
import PyPDF2
from tkinter.filedialog import *

## OPENS FINDER WINDOW. PICK PDF FILE.

book_file = askopenfilename()

## Use PyPDF2 library to manage/manipulate PDF files

pdf_reader = PyPDF2.PdfFileReader(book_file)
number_of_pages = pdf_reader.getNumPages()

## pyttsx3 library converts text to speech

for num in range(0, number_of_pages):
    page = pdf_reader.getPage(num)
    text = page.extractText()
    speech_reader = pyttsx3.init()
    speech_reader.say(text)
    speech_reader.runAndWait()













