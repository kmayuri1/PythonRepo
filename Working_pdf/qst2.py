# 2. What modes do the File objects for PdfFileReader() and PdfFileWriter() need to be opened in?
print('For PdffileReader() file object is read-binary (rb) and PdffileWriter() the file object is write-binary(wb)')


import PyPDF2
pyobj=open('Riddhi_1421013.csv','rb')
pdfReader=PyPDF2.PdfFileReader(pyobj)
pageobj=pdfReader.getPage(0)

pdfWriter=PyPDF2.PdfFileWriter()
pdfWriter.addPage(pageobj)
result=open('Riddhi_1421013.csv','wb')
pdfWriter.write(result)
result.close()
pyobj.close()