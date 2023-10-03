#16. How do you make a regular expression case-insensitive?

import re

regx=re.compile(r'HeLLo',re.IGNORECASE)
pattern=regx.search('Hey,HELLO all how are you!!').group()
print(pattern)