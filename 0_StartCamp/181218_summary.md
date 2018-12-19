# 181218 수업정리 (ctrl + 1 큰제목)

## 1. 개발환경 설정 (ctrl +2)

* chocolatey (* + space bar)
  * 윈도우 패키지 매니저 (tab)
* python -v 3.6.7
* git
  *  Version Control System
* vscode
  * Code Editor
* chrome
* python function documentatiom => 공식 문서에서 function을 검색함

## 2. 용어정리

* cd : change diectory

* ls : list

* mkdir : make directory

* rmdir : remove directory

* touch : make file

* ctrl + l : refresh

* exit()

* ↑ :  전 명령어

* pip install :  위치에 상관 없이 설치

* ls -a : 모두 보여줌

* ``` python
  (```+enter : code box, `` : code line)
  numbers = list(range(100)) #0부터 99까지
  numbers = list(range(0, 100))
  numbers = [1: 100] #[start: end] => start는 포함, end는 안포함
  ```

* 접근 => 무조건 대괄호

* ```python
  hphk = [
      {
          'name' : 'John',
          'email' : 'ryeong@ssafy.com'
      },
      {
          'name' : 'Sam',
          'email' : 'sam@ssafy.com'
      },
      {
          'name' : 'Tak',
          'email' : 'Tak@ssafy.com'
      }
  ]
   #접근 => hphk[0]['name']
   #dictionary = {'key(90%는 string)' : 'value'(type 상관X)}
  ```

* `list(처음:끝+1)` => 슬라이싱, list형을 가짐

* `n = n + 1 == n += 1` //  기호가 붙어있을 경우 =이 항상 뒤에 옴

* ```python
  del(team[2]) #team[2] 삭제
  len(team) #team의 index 갯수
  ```

### Function

### Method

```python
scores = [45, 60, 78, 88]
high_score = max(scores) #최댓값
low_score = min(scores) #최솟값
round(1.876, 2) # 소수점 2번째 자리까지 반올림
help(funtion name) #funcion에 대한 도움말

first = [11.25, 18.0, 20.0]
second = [10.75, 9.50]

#full에 first와 second를 합쳐서 저장
full = first + second
# full_sorted에 full을 오름차순으로 정렬해서 저장
full_sorted = sorted(full)
# full_sorted에 full을 내림차순으로 정렬해서 저장
full_sorted = sorted(full, reverse = True)
```

```python
my_list = [4, 7, 9, 1, 3, 6]
#최댓값/최솟값
max(my_list)
min(my_list)

#특정 요소의 인덱스
my_list.index()
#리스트 거꾸로 배열
my_list.reverse()

dust = 100 #int
lang = 'python' #str
lang.capitalize() #첫번째 원소를 대문자로 변환, lang은 바뀌지 않음
lang.replace('on', 'off') #on을 off로 변환, lang은 바뀌지 않음

samsung = ['elec', 'sds', 's1'] #list
samsung.index('sds') #'sds'의 index
samsung.append('bio') # == samsung + ['bio'] , 원본이 바뀜 return은 없음
```

| str      | int   | list           | bool  |
| -------- | ----- | -------------- | ----- |
| `python` | `100` | `'a', 3, true` | False |

### URL

```python
import webbrowser #선언은 앞에

keywords = [
    'george',
    'monni'
]

for keyword in keywords:
    url = 'https://www.google.com/search?q=' + keyword #url 검색
    webbrowser.open_new(url) 
```

```python
import requests

url = 'https://www.nlotto.co.kr/common.do?method=getLottoNumber&drwNo=837'

response = requests.get(url, verify = False) 
#인증서에 대한 검사는 하지 않고 불러옴(생략가능)
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

```

```python
from darksky import forecast

multicampus = forecast('1da2bc199dfc2330861109b5bb96535f', 37.501503, 127.039606)

print(multicampus['currently']['summary'])
print(multicampus['currently']['temperature'])



# import requests

# url = 'https://api.darksky.net/forecast/1da2bc199dfc2330861109b5bb96535f/37.501503,127.039606'

# res = requests.get(url)
# data = res.json()

# print(data['currently']['summary'])
```

