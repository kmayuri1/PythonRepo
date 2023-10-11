# 4. What method takes a list argument and writes it to a CSV file?

print('The writerow() method for writer objects takes a list argument')

import csv
fileobj=open('output1.csv','w',newline='')
otWriter=csv.writer(fileobj)
otWriter.writerow(['hi','hello','gm','Hey'])
otWriter.writerow(['Great','good','stop'])
fileobj.close()