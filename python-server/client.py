import requests

data = requests.post("http://127.0.0.1:5000/", params={
    "text": "text"
}, timeout=10)

print(data.json())