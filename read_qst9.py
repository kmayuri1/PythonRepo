# 9. What happens if an existing file is opened in write mode?

file3=open(r'C:\Users\mayur\Python_3oct\Read_Write\oct3.txt', 'w')
print(file3.write('HelloWelcome'))

file3=open(r'C:\Users\mayur\Python_3oct\Read_Write\oct3.txt','r')
print(file3.read())
print('if an existing file is opened in write mode then it will overwrite the data.')