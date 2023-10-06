# 5. How do you save a requests response to a file?

import requests
res=requests.get('https://automatetheboringstuff.com/files/rj.txt')
res.raise_for_status()
f1=open('RomeoAndJuliet.txt', 'wb')
for data in f1.iter_content(100000):
    f1.write(data)
 
f1.close()   