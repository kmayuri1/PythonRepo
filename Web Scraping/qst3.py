# 3. What requests method checks that the download worked?

print('raise_for status()method is used to check the download works successfully or not')

import requests
res =requests.get('https://automatetheboringstuff.com/files/rj.txt')
res.raise_for_status()
print(res.raise_for_status())