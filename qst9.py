#9. What two things does the ? character signify in regular expressions?

import re

regx=re.compile(r'Best(wo)?man')
pattern=regx.search('Bestman')
print(pattern)