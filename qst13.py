#13. What do the \D, \W, and \S shorthand character classes signify in regular expressions?

import re

regx=re.compile(r'\D\S\W')
pattern=regx.findall('hi@llo, w$lcom e, goo!!morning')
print(pattern)

regx1=re.compile(r'\D+\S\W+')
pattern1=regx1.findall('hi@llo, w$lcom e, goo!!morning')
print(pattern1)

print('\D --is used to match any character')
print('\W --is used to match any character which is not a letter, numeric digit, or the underscore character.')
print('\S --is used to match any character which is not a space, tab, or newline')