import requests

url = 'https://www.nlotto.co.kr/common.do?method=getLottoNumber&drwNo=837'

response = requests.get(url, verify = False) #인증서에 대한 검사는 하지 않고 불러옴(생략가능)
lotto_data = response.json() # dic형

real_numbers = []

for key, value in lotto_data.items(): # item(): key와 value를 함께 추출함
    if 'drwtNo' in key:
        real_numbers.append(value) 

real_numbers.sort()
bonus_number = lotto_data['bnusNo']
print(real_numbers)

# my_numbers, real_numbers, bonus_number
# 1등 : my_numbers == real_numbers
if my_numbers == real_numbers :
    print('1등입니다 예~~~~!!!!')

    
# 2등 : real & my가 5개 같고, my의 나머지 하나가 bonus_number
# 3등 : real & my가 5개 같다
# 4등 : real & my가 4개 같다
# 5등 : real & my가 3개 같다