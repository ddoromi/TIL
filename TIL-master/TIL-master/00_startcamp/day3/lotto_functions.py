import requests
import random

def pick_lotto():
    numbers = random.sample(range(1, 46), 6)
    return numbers

def get_lotto(draw_no):
    url = 'https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=' + str(draw_no)

    response = requests.get(url)
    lotto_data = response.json()

    numbers = []
    for key, value in lotto_data.items():
        if 'drwtNo' in key:
            numbers.append(value)

    numbers.sort()
    bonus_number = lotto_data['bnusNo']
    
    final_dict = {
        'numbers': numbers,
        'bonus': bonus_number
    }
    
    return final_dict 

def am_i_lucky(pick, draw):
    match = set(pick) & set(draw['numbers'])
    if len(match) == 6:
        return('1등')
    elif len(match) == 5 and draw['bonus'] in pick:
        return('2등')
    elif len(match) == 5:
        return('3등')
    elif len(match) == 4:
        return('4등')
    elif len(match) == 3:
        return('5등')
    else:
        return('꽝')













# match_count = len(my_numbers & real_numbers)

# if match_count == 6:
#     print('1등')
# elif match_count == 5 and bonus_number in my_numbers:
#     print('2등')
# elif match_count == 5:
#     print('3등')
# elif match_count == 4:
#     print('4등')
# elif match_count == 3:
#     print('5등')
# else:
#     print('꽝')