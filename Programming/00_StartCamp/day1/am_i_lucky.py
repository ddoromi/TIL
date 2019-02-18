import requests
import random



url = 'https://www.nlotto.co.kr/common.do?method=getLottoNumber&drwNo=837'

response = requests.get(url, verify = False) #인증서에 대한 검사는 하지 않고 불러옴(생략가능)
lotto_data = response.json() # dic형

real_numbers = set([])

for key, value in lotto_data.items(): # item(): key와 value를 함께 추출함
    if 'drwtNo' in key:
        real_numbers.add(value) 

bonus_number = lotto_data['bnusNo']


if my_numbers == real_numbers :
    print('1등 입니다. 예~~~~~~~~~~~~~~~~~~~')
else :
    if len(real_numbers & my_numbers) == 4 :
        print('3등 입니다. 예~~~~~~~~~~~~~~~~~~~')
    elif len(real_numbers & my_numbers) == 3 :
        print('4등 입니다. 예~~~~~~~~~~~~~~~~~~~')
    else :
        real_numbers.add(bonus_number)
        if len(real_numbers & my_numbers) == 6 :
            print('2등 입니다. 예~~~~~~~~~~~~~~~~~~~')
        else :
            print('꽝 입니다. 예~~~~~~~~~~~~~~~~~~~')

# count = 0
# while(1):
#     my_numbers = (random.sample(range(1, 47), 6))
#     my_numbers = set(my_numbers)
#     count += 1
#     print(count)

#     if my_numbers == real_numbers :
#         print('1등 입니다. 예~~~~~~~~~~~~~~~~~~~')
#         break
#     else :
#         if len(real_numbers & my_numbers) == 4 :
#             print('3등 입니다. 예~~~~~~~~~~~~~~~~~~~')
#         elif len(real_numbers & my_numbers) == 3 :
#             print('4등 입니다. 예~~~~~~~~~~~~~~~~~~~')
#         else :
#             real_numbers.add(bonus_number)
#             if len(real_numbers & my_numbers) == 6 :
#                 print('2등 입니다. 예~~~~~~~~~~~~~~~~~~~')
#             else :
#                 print('꽝 입니다. 예~~~~~~~~~~~~~~~~~~~')


#비교할 때 많이 쓰이는 구조
# for my_numbers in my_numbers:
#     for real_numbers in real_numbers:
#         if my_numbers == real_numbers:
#             count += 1

# if count == 6:
#     print(1)
# elif count == 5 and bonus in my_numbers:
#     print(2)
# elif count == 5:
#     print(3)


