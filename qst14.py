#14. What is the difference between .* and .*??

import re

regx=re.compile(r'Name:(.*)')
pattern=regx.search('Name:helloman, how are you')
print(pattern.group(0))

regx1=re.compile(r'Name:(.*?)')
pattern1=regx1.search('Name:helloman, how are you')
print(pattern1.group())

print('.* is used to match all pattern whereas .*? is used to match min of pattern')

