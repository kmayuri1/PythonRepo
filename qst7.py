#7. The findall() method returns a list of strings or a list of tuples of strings. What makes it return one or the other?

import re
regx=re.compile(r'\d\d\d-\d\d-\d\d\d\d')
pattern=regx.findall('123-11-1234')
print('pattern with list of strings is:',pattern)

regx1=re.compile(r'(\d\d)-(\d\d)-(\d\d\d)')
pattern1=regx1.findall('11-22-112')
print('pattern with list of tuples is:',pattern1)

