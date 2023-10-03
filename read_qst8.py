# 8. What are the three “mode” arguments that can be passed to the open() function?



file2=open(r'C:\Users\mayur\Python_3oct\Read_Write\oct3.txt', 'w')
print(file2.write('Hello'))

file3=open(r'C:\Users\mayur\Python_3oct\Read_Write\oct3.txt', 'a')
print(file3.write('Hey,How are you'))

file3=open(r'C:\Users\mayur\Python_3oct\Read_Write\oct3.txt', 'r')
print(file3.read())