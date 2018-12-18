import requests

url = 'https://www.nlotto.co.kr/common.do?method=getLottoNumber&drwNo=837'

response = requests.get(url, verify = False) #인증서에 대한 검사는 하지 않고 불러옴(생략가능)
lotto_data = response.json() # dic형

real_numbers = []

# for key in lotto_data:
#     if 'drwtNo' in key:
#         real_numbers.append(lotto_data[key]) 

for key, value in lotto_data.items(): # item(): key와 value를 함께 추출함
    if 'drwtNo' in key:
        real_numbers.append(value) 

real_numbers.sort()
bonus_number = lotto_data['bnusNo']
print(real_numbers)

# real_numbers = [
#     lotto_data['drwtNo1'],
#     lotto_data['drwtNo2'],
#     lotto_data['drwtNo3'],
#     lotto_data['drwtNo4'],
#     lotto_data['drwtNo5'],
#     lotto_data['drwtNo6'],
# ] ctrl + / : 선택한 부분을 주석처리함

#print(real_numbers)
