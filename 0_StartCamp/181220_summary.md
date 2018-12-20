# 181220 수업정리

# 1. HTML

* 보여지는 것은 브라우저 영역(스타일 시트), 역할 지정은  html.
* 클라이언트 사이드 : 브라우저, 어플리케이션

* h1 : 가장 큰 제목, 중요한 제목

## 2. Python

### Lotto Code

```python
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
```

```python
#list = [1, 2, 3]
#dict = {key : [1, 2, 3]}
#set = {1, 2, 3} : 순서(index)가 없음
```



* 함수 정의하기

```python
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

    bonus_number = lotto_data['bnusNo']

    lotto_number = {'real' : real, 'bonus' : bonus_number}
    print(lotto_number)

    return lotto_number

def pick_lotto():
    numbers = random.sample(range(1, 46), 6)
    print (numbers)
    return numbers

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
real_numbers = get_lotto(1)
my_numbers = pick_lotto()
print(am_i_lucky(my_numbers, real_numbers))
```

### check_lotto

```python
from lotto_functions import am_i_lucky, pick_lotto, get_lotto

print(am_i_lucky(pick_lotto(), get_lotto(837)))
```

* set()
  * 집합 선언 : name = set()

  * & : 교집합, - : 차집합
  * set에 추가하는 메소드 : add(value) / list에 추가하는 메소드 : append(value)
* def 함수이름() : 함수 정의
* 함수(arguments(인자, args)) :  함수 호출
* return : 함수의 반환값
* sorted() : 원본을 파괴하고 정열함 + return 값 O , 메소드 사용 X
* sort() : 원본을 파괴하고 정열함 + return 값 X, 메소드 사용 O 

### Math_functions

```python
print(__name__) 

def average(numbers):
     return sum(numbers) / len(numbers)

def cube(x):
    return x * x * x

def main():
    my_score = [79, 84, 66, 93]
    print('평균:', average(my_score))
    print(cube(3))

if __name__ == 'main' :
    main()
```

### do_math

```python
print(__name__)
# import math_functions

# print(mathfunctions.cube(5))
# print(math_functions.average([1, 6, 8]))

from math_functions import cube, average

print(cube(5))
print(average([1, 7, 40]))
```



## *

* crtl+c : 실행 멈춤
* convention : 관습으로 행해지는 것 
* 리펙토링 : 기능이나 성능에 대한 변화는 없지만 좀 더 명확한 의미를 가지도록 바꾸는 것