# 181218 수업정리

## 1. 개발환경 설정

* chocolatey/
  * 윈도우 패키지 매니저
* python -V 3.6.7
* git 
  * Version Control System
* vscode
  * Code Editor
* chrome
  * Browser

## 2. list

### list 만들기

```python
mcu = [
    ['ironman', 'captain america', 'dr.strange'], 
    ['xmen', 'deadpool'],
    ['spiderman']
]
disney = mcu[0]
dr_strange = disney[2]
dr_strange = mcu[0][2]
```

이때 `'dr.strange'` 에 접근하려면 어떻게 해야할까?

리스트 안에 리스트가 있다! 

### list 추출하기

1. `[0]` 처럼 인덱스 접근하기
2. `[1:10]` 처럼 잘라내기

### list 연산

```python
team = [
    'john', 10000,
    'neo', 100,
    'tak', 40500,
]

new_member = ['js', 10]

team = team + new_member
team += new_member

```



## 3. dict

```python
my_info = { 
    'name': 'neo',
    'job': 'hacker',
    'mobile': '01012345678',
    'email': 'neo@hphk.kr' 
}

hphk = [
    {
        'name': 'john',
        'email': 'john@hphk.io'
    },
    {
        'name': 'neo',
        'email': 'neo@hphk.io'
    },
    {
        'name': 'tak',
        'email': 'tak@hphk.io'
        'married': False
    }
]

type(hphk) # list

p = hphk[2]
p['name']

hphk[2]['name']
```



## 4. Function

```python
print('hi')
len('hi') # 2
len([1,2,3,4,5]) # 5
type('a')

scores = [45, 60, 78, 88]
high_score = max(scores)
lowest_score = min(scores)
round(1.8)
round(1.876, 2)

first = [11.25, 18.0, 20.0]
second = [10.75, 9.50]

# full 에 first 와 second 을 합쳐서 저장

# full_sorted 에 full 을 오름차순으로 정렬해서 저장
full_sorted = sorted(full)

# *reverse_sorted 에 full 을 내림차순으로 정렬해서 저장
reverse_sorted = sorted(full, reverse=True)
```

## 5. Method

메서드는 함수다! 다만 **[주어].동사()** 의 형식으로 이루어 지며, [주어] 자리에 오는 object 들이 할 수 있는 행동(함수)들이다.

```python
my_list = [4, 7, 9, 1, 3, 6]
# 최대/최소
max(my_list)
min(my_list)
# 특정 요소의 인덱스?
my_list.index()
# 리스트를 뒤집으려면?
my_list.reverse()

dust = 100 # <class: int>
lang = 'python' # str
samsung = ['elec', 'sds', 's1'] # list

lang.capitalize()
lang.replace('on', 'off')

samsung.index('sds')
saumsung.append('bio') # 원본이 바뀐다!
```





| str        | int   | list             | bool    | <= Class  |
| ---------- | ----- | ---------------- | ------- | --------- |
| `'python'` | `100` | `['a', 3, True]` | `False` | <= Object |



