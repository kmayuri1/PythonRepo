#11. What is the difference between {3} and {3,5} in regular expressions?

import re

regx=re.compile(r'(AA){3}')
pattern=regx.search('AAAAAAAA')
print(pattern.group())


regx1=re.compile(r'(B){3,5}')
pattern1=regx1.search('BBBBBB')
print(pattern1.group())
