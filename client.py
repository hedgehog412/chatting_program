import requests


response = requests.get("http://127.0.0.1:5000")

print response.text

response = requests.get("http://127.0.0.1:5000/bye")
print response.text
