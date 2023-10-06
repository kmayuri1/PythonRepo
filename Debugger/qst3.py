# 3. Write an assert statement that always triggers an AssertionError.

def addition():
    a=input('Enter Number:')
    b=input('Enter Number:')
    assert False 
    add=a+b
    return add

result=addition()
print(result)    