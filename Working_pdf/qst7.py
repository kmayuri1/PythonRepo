
# 7. What method returns a Document object for a file named demo.docx?


print('demo.docx method returns a Document object for file.')

import docx
doc=docx.Document('demo.docx')
print(doc.paragraphs[0].text)
