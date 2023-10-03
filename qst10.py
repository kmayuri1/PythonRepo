#10. What is the difference between the + and * characters in regular expressions?

import re
regx=re.compile(r'He(llo)+man')
pattern=regx.search('he adventures of Heman')
print(pattern.group())
regx2=re.compile(r'He(llo)+man')
pattern2=regx2.search('he adventures of Helloman')
print(pattern2.group())

regx1=re.compile(r'he(llo)*man')
pattern1=regx1.search('he adventures of helloman')
print(pattern1.group())

print('+ character is used to match atleast one or more preseding group where as * character is used to fine zero or more preseding group')