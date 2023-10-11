# 5. What do the delimiter and lineterminator keyword arguments do?

print('The delimiter is the character that appears between cells \n The Lineterminator is the character that comes at the end of row')

import csv
fileobj=open('exam.csv','w',newline='')
csvWriter=csv.writer(fileobj,delimiter='\t',lineterminator='\n\n\n')
csvWriter.writerow(['apples', 'oranges', 'grapes'])
csvWriter.writerow(['eggs', 'bacon', 'ham'])
csvWriter.writerow(['Hi','Hello','Hi','Hello'])
fileobj.close()
             