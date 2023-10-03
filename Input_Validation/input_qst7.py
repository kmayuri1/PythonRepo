# 7. What does inputStr(limit=3, default='hello') do if blank input is entered three times?

import pyinputplus as pyip
pattern=pyip.inputStr('Enter Name',limit=3, default='hello')
print(pattern)
print("If we entered blank input 3 times by giving default='hello'after 3rd it will  print 'hello'")