from darksky import forecast

multicampus = forecast('1da2bc199dfc2330861109b5bb96535f', 37.501503, 127.039606)

print(multicampus['currently']['summary'])
print(multicampus['currently']['temperature'])



# import requests

# url = 'https://api.darksky.net/forecast/1da2bc199dfc2330861109b5bb96535f/37.501503,127.039606'

# res = requests.get(url)
# data = res.json()

# print(data['currently']['summary'])

