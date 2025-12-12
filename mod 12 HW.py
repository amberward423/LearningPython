#Problem 1
import requests,json

print("Do you want to hear a joke?")

request = "https://api.chucknorris.io/jokes/random"

response = requests.get(request).json()

print(response['value'])

