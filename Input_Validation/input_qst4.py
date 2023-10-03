# 4. How can you ensure that the user enters a whole number between 0 and 99 using PyInputPlus?

import pyinputplus as pyip
pattern=pyip.inputNum('Enter Num:',min=0,max=99)
print(pattern)
