import requests
url = 'http://localhost:8000'
myData = {'name': 'van Rossum'}

x = requests.post(url, json = myData)
print(x.text)
