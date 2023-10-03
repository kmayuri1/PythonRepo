#3. What does the search() method return?

import re

regx=re.compile(r'\d\d\d-\d\d\-\d\d\d')
pattern=regx.search('My nbr is 123-11-123')
print('Nbr is:'+pattern.group())

print('Search() method match the pattern which we required to match')
