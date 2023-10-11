#5. If a PdfFileReader object’s PDF is encrypted with the password swordfish, what must you do before you can obtain Page objects from it?

print('If PdfFileReader object is encrypted format then to obtain the PDF object we have to decrypt it')

import PyPDF2
f1obj=open('Riddhi_1421013.pdf','wb')
pdfWriter=PyPDF2.encrypt('Ridhisha')
resultPdf=open('encryptedpf.pdf','wb')
pdfWriter.write(resultPdf)

resultPdf.close()
pdfReader=PyPDF2.PdfFileReader(open('encryptedpf.pdf','rb'))
readobj=pdfReader.decrypt('Ridhisha')
pageobj=readobj.getPage(0)
