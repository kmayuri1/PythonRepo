# 6. What methods do you use to rotate a page?


print('rotateClockwise() and rotateCounterClockwise() methods and how much degree we want to rotate that we have to give in integer')

import PyPDF2
f1=open('Riddhi_1421013.pdf','rb')
f1obj=PyPDF2.PdfReader(f1)
p1=f1obj.pages[0]
print(p1)
p1.rotate(90)
pdfWriter=PyPDF2.PdfWriter()
pdfWriter.add_page(p1)
resultPdfFile=open('rotate90.pdf','wb')
pdfWriter.write(resultPdfFile)
resultPdfFile.close()
f1.close()