#5. In the regex created from r'(\d\d\d)-(\d\d\d-\d\d\d\d)', what does group 0 cover? Group 1? Group 2?

import re
regx=re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
pattern=regx.search('My nbr is 123-111-2323')
print('Group 0 covers:'+pattern.group(0))
print('Group 1 covers:'+pattern.group(1))
print('Group 2 covers:'+pattern.group(2))