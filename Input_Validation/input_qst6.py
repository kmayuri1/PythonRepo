# 6. What does inputStr(limit=3) do if blank input is entered three times?

import pyinputplus as pyip
pattern=pyip.inputStr('Enter Name :',limit=3,default='N/A')
print(pattern)
print('if we enter blank input 3 times then after three it throws Excepetion message.To avoid exception message we can give (Blank=N/A)')