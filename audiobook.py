import pyttsx3
import PyPDF2

book = open('tt1.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(book)
pages = pdfReader.numPages
print('Total number of pages:', pages)
speaker = pyttsx3.init()
for num in range(0, pages):
    page = pdfReader.getPage(0)
    text = page.extractText()
    speaker.say('Hello friend! I can read the pdf for you. here it is written that')
    speaker.say(text)
    speaker.runAndWait()
