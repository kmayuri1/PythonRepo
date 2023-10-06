# 7. What line of code can you add to disable all logging messages in your program?

import logging

def addition():
    a=input('Enter value of a :')
    b=input('Enter value of b :')
    
    if int(a) <1:
        logging.error('Value of a is less than b')
    elif int(b) >100:
        logging.warning('Value of b exceeds the boundary value')
       
    else: 
        logging.info('Values of a and b are within range')
    add = a + b    
    return add
# logging.disable(logging.CRITICAL)
logging.info('Program Started')
result=addition()
print(result)           



