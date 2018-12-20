import requests
import random

#함수 정의
def get_lotto(draw_no):
    #url은 string이기 때문에 type을 일치시켜줘야 함, int -> string으로 변환
    url = 'https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo='+ str(draw_no)

    response = requests.get(url) #인증서에 대한 검사는 하지 않고 불러옴(생략가능)
    lotto_data = response.json() # dic형

    real = []
    for key, value in lotto_data.items(): # item(): key와 value를 함께 추출함
        if 'drwtNo' in key:
            real.append(value) 
    return {'real' : real, 'bonus' : lotto_data['bnusNo']}

def pick_lotto():
    return random.sample(range(1, 46), 6)

# 내가 짠 코드 -> list로 for문 돌려서 비교
# def am_i_lucky(my_numbers, real_numbers):
#     count = 0 #변수가 처음 나올 때 초기화 해주기!!!!!!!!
#     for my_number in my_numbers:
#         for real_number in real_numbers['real']:
#             if my_number == real_number:
#                 count += 1
#     if count == 6:
#         print('1등입니다 예~~~~~~~~~~~~~')
#     elif count == 5 and bonus in my_numbers:
#         print('2등입니다 예~~~~~~~~~~~~~')
#     elif count == 5:
#         print('3등입니다 예~~~~~~~~~~~~~')
#     elif count == 4:
#         print('4등입니다 예~~~~~~~~~~~~~')
#     else:
#         print('꽝')

# 강사님이 짜주신 코드 -> set의 교집합을 사용해서 비교
def am_i_lucky(my_numbers, real_numbers):
    if len(set(my_numbers) & set(real_numbers)) == 6:
        return('1등입니다')
    elif len(set(my_numbers) & set(real_numbers)) == 5 & real_numbers['bonus'] in my_numbers:
        return('2등입니다')
    elif len(set(my_numbers) & set(real_numbers)) == 5:
        return('3등입니다')
    elif len(set(my_numbers) & set(real_numbers)) == 4:
        return('5등입니다')
    else:
        return('꽝')

#함수 호출
#print(am_i_lucky(pick_lotto(), get_lotto(1)))