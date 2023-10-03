#1. What is the function that creates Regex objects?

import re

con=re.compile(r'Hello')
con.sub('Hi','Hey Hello,How are you!!')
print(con.sub('Hi','Hey Hello,How are you!!'))
