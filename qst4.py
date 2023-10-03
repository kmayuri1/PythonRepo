#4. How do you get the actual strings that match the pattern from a Match object?

import re
regx=re.compile(r'\[\d\d\]-\d\d-\d\d')
pattern=regx.search('pattern is [12]-34-56')
print('My pattern is:'+pattern.group())