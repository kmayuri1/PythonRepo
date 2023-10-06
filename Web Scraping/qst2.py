#2. What type of object is returned by requests.get()? How can you access the downloaded content as a string value?

print('requests.get() returns a response object and which having text attribute that contains the downloaded string')

import requests
res =requests.get('https://automatetheboringstuff.com/files/rj.txt')
type(res)