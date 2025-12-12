import requests, json
lat= input("Enter latitude: ")
lon = input("Enter longitude: ")
API_key= "9d13ea3e43a31fcd6e3d2faf99db6653"
headers={
    "Authorization": "Bearer API_KEY"
}

request = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_key}"
response = requests.get(request)

info = response.json()

kelvin = info["main"]["temp"]
celsius = kelvin - 273.15

print(info)
print(celsius)


#response = requests.get(request, headers=headers).json()

print(response)

#def Convert(temperature):
#    for i in temperature:
#        celsius = a
#        kelvin = b
#        a = b - 273.15
#print(f"The Temperature in Kelvins is {b} and in Celsius is {a}")
