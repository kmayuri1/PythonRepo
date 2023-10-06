# 4. How can you get the HTTP status code of a requests response?

print('by using status_codes we can get requests response')

import requests

res =requests.get('https://automatetheboringstuff.com/files/rj.txt')
type(res)
res.status_code==requests.codes.ok
print(res.text[:300])