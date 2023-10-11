#1. A string value of the PDF filename is not passed to the PyPDF2.PdfFileReader() function. What do you pass to the function instead?

print('It passes the file object which returns from open() function')

import PyPDF2
pyobj=open('Riddhi_1421013.csv','rb')
pdfReader=PyPDF2.PdfFileReader(pyobj)
pageobj=pdfReader.getPage(0)
print(pageobj.extract_text())
