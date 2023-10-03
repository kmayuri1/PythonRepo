#20. How would you write a regex that matches a number with commas for every three digits? It must match the following:

# '42'
# '1,234'
# '6,368,745'
# but not the following:

# '12,34,567' (which has only two digits between the commas)
# '1234' (which lacks commas)


import re
regx=re.compile(r'^\d{1,3}(,\d{3})*$')
pattern=regx.search('6,368,745')
pattern1=regx.search('12,34,567')
print(pattern)
print(pattern1)

regx1=re.compile(r'^\d{3}(,\d{3})*$')
pattern2=regx1.search('6,368,745')
pattern3=regx1.search('123,343,567')
print(pattern2)
print(pattern3)