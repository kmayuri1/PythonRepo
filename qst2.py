#2. Why are raw strings often used when creating Regex objects?
import re

reg=re.compile(r'\(\d\d\)-\d\d')
reg.search('(12)-12')
print(reg.search('(12)-12'))
print('By using raw strings as its easy to use and whatever strings we have to escape we can escape easily')
