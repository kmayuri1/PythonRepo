# 1. Write an assert statement that triggers an AssertionError if the variable spam is an integer less than 10.

import random

def addition():
    a=random.randint(1, 20)
    # spam=random.randint(15,20)
    spam=random.randint(1,10)
    assert spam >= 10
    add =a + spam
    return add
result=addition() 
print(result)   
     
