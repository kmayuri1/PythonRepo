#15. What is the character class syntax to match all numbers and lowercase letters?

import re
regx=re.compile(r'[0-9a-z]' )
pattern=regx.findall('AbcDHJ12fgRT@ar')
print(pattern)