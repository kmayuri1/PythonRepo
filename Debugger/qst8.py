#8. Why is using logging messages better than using print() to display the same message?

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

print('In above function by giving only logging.CRITICAL will disabled all logging message whereas using print function we have to remove one by one and its time consuming and we have to go thr all code.')

