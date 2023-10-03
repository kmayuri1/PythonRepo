#12. What do the \d, \w, and \s shorthand character classes signify in regular expressions?

import re

regx=re.compile(r'\d+\s\w+')
pattern=regx.findall('12 drummers, 11 pipers, 10 lords')
print(pattern)

regx1=re.compile(r'\d\s\w')
pattern1=regx1.findall('12 drummers, 11 pipers, 10 lords')
print(pattern1)

print('\d is used to match only digits')
print('\w is used to match digits,letters and underscore')
print('\s is used to match spaces,tab and newline')