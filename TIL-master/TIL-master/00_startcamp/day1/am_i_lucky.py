import requests
import random

url = 'https://www.nlotto.co.kr/common.do?method=getLottoNumber&drwNo=837'

response = requests.get(url, verify=False)
lotto_data = response.json()

real_numbers = []
for key, value in lotto_data.items():
    if 'drwtNo' in key:
        real_numbers.append(value)

real_numbers.sort()
real_numbers = set(real_numbers)
bonus_number = lotto_data['bnusNo']

match_count = len(my_numbers & real_numbers)

if match_count == 6:
    print('1등')
elif match_count == 5 and bonus_number in my_numbers:
    print('2등')
elif match_count == 5:
    print('3등')
elif match_count == 4:
    print('4등')
elif match_count == 3:
    print('5등')
else:
    print('꽝')