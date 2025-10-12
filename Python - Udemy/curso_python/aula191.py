# requests para requisição de HTTP
# Tutorial -> https://youtu.be/Qd8JT0bnJGs
import requests

url = "http://localhost:8000/"
response = requests.get(url)
print(response.status_code)
print(response.headers)
