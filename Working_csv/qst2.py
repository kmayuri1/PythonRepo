# 2. What do you pass to csv.reader() and csv.writer() to create reader and writer objects?

print('File object to open the file')

import csv
fileobj=open('example1.csv')
f1Reader=csv.reader(fileobj)
f1data=list(f1Reader)
print(f1data)

