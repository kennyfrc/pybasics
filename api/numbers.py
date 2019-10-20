import requests

response = requests.get("http://numbersapi.com/random/math")

print(response.text)