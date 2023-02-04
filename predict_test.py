import requests
import json

url = 'http://localhost:9696/predict'
data = 'https://m.media-amazon.com/images/I/51aAu04384L.jpg'
img_url = {'img_url': data}
headers = {'Content-type': 'application/json'}
response = requests.post(url, data=json.dumps(img_url),headers=headers)
result = response.json()
print(result)

