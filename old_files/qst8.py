#8. What does the | character signify in regular expressions?

import re
regx=re.compile(r'Hi |Hello')
pattern=regx.search('Hey Hi,Hello all welcome!!')
print('| character signifies :'+pattern.group())
print('| character is used to match either this or that from the string')