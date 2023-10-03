# 10. What is the difference between the read() and readlines() methods?

file5=open(r'C:\Users\mayur\Python_3oct\Read_Write\oct3_1.txt','w')
file5.write('Welcome')

file5=open(r'C:\Users\mayur\Python_3oct\Read_Write\oct3_1.txt','r')
print(file5.read())

file6=open(r'C:\Users\mayur\Python_3oct\Read_Write\oct3_2.txt','w')
file6.write("""When, in disgrace with fortune and men's eyes,
I all alone beweep my outcast state,
And trouble deaf heaven with my bootless cries,
And look upon myself and curse my fate""")
file6=open(r'C:\Users\mayur\Python_3oct\Read_Write\oct3_2.txt','r')
print(file6.readlines())