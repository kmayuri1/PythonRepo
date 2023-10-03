# 17. What does the . character normally match? What does it match if re.DOTALL is passed as the second argument to re.compile()?

import re

regx=re.compile(r'.at')
pattern=regx.findall('The fat cat sat on wall at!! ')
print(pattern)

regx1=re.compile('.*',re.DOTALL)
pattern1=regx1.search('''The fat cat sat on wall at!
                       Hello all,how are you..''').group()
print(pattern1)