from darksky import forecast

multicampus = forecast('316b59dc6de6bb4d984f417b77db67b7', 37.501311, 127.037471)

print(multicampus['currently']['summary'])
print(multicampus['currently']['temperature'])

# import requests

# url = 'https://api.darksky.net/forecast/316b59dc6de6bb4d984f417b77db67b7/37.501311,127.037471'

# res = requests.get(url)
# data = res.json()

# print(data['currently']['summary'])
