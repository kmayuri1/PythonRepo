# 13. How do you add a paragraph with the text 'Hello, there!' to a Document object stored in a variable named doc?


import docx
doc = docx.Document()
doc.add_paragraph('Hello, there!')

doc.save('hello.docx')