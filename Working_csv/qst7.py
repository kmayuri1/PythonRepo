# 7. What function takes a Python data structure and returns a string of JSON data?

print('json.dumps() takes python data structure and returns a string of json data')

pythonValue = {'isCat': True, 'miceCaught': 0, 'name': 'Zophie',
'felineIQ': None}
import json
stringOfJsonData = json.dumps(pythonValue)
print(stringOfJsonData)