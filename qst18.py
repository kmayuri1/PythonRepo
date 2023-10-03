#18. If numRegex = re.compile(r'\d+'), what will numRegex.sub('X', '12 drummers, 11 pipers, five rings, 3 hens') return?

import re
regx=re.compile(r'\d+')
pattern=regx.sub('X', '12 drummers, 11 pipers, five rings, 3 hens') 
print(pattern)
print('\d+ will return \d is used to match only digits so whereever it matches the digits over there it will replaces X,means pattern to match.')
