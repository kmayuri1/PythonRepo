# 3. How do you acquire a Page object for page 5 from a PdfFileReader object?

print('By calling getPage(4) will get page 5')

import PyPDF2
pyobj=open('Riddhi_1421013.csv','rb')
objReader=PyPDF2.PdfFileReader(pyobj)
print(pageobj=objReader.getPage(4))
