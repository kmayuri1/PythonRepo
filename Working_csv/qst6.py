# 6. What function takes a string of JSON data and returns a Python data structure?

print('json.loads function used to take string of json data')
data='{"name": "Zophie", "isCat": true,"miceCaught": 0, "napsTaken": 37.5, "felineIQ": null }'
import json
fileobj=json.loads(data)
print(fileobj)

