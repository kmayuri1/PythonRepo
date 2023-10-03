# 5. What is passed to the allowRegexes and blockRegexes keyword arguments?

import pyinputplus as pyip
pattern=pyip.inputNum('Enter Num :',allowRegexes=[r'\d\d\d\w+'])
pattern1=pyip.inputNum('Enter Num :',blockRegexes=[r'[12345]'])
print(pattern)
print(pattern1)