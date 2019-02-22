##### 07_day [19.02.22]

# 4. Stack_01

## 1. 스택

* 저장된 자료는 선형 구조를 가짐.
* 마지막에 삽입한 자료를 가장 먼저 꺼냄. => 후입선출

#### 필요한 자료구조와 연산

##### 1. 자료구조

* C언어에서는 배열 사용
* 저장소 자체를 스택이라 부름.
* 마지막 삽입된 원소의 위치를 top이라 부름.

##### 2. 연산

* 삽입(push): 저장소에 자료 저장
* 삭제(pop): 저장소에서 자료를 꺼냄
* isEmpty : 공백인지 확인
* peek : top에 있는 item을 반환

#### 스택의 구현

```python
# 리스트를 스택으로 사용
s = []

for i in range(5):
    s.append(i)
    
while len(S) > 0:
    print(S.pop(-1))
```





## 2. 재귀호출

* 자기 자신을 호출하여 순환 수행되는 것
* 점화식 필요

#### 구현

* DFS(깊이 우선 탐색), 분할 정복, 트리 순회 
* 백트래킹, 동적계획법(재귀적 DP)

```python
# factorial
def fact(n):
    if n <= 1:
        return 1
    else:
        return n * fact(n-1)
    print(fact(5))
```

```python
cnt = 0
bit = [0] * 3 # 비트 표현 가능

def printHello(i, n):
    global cnt
    if i == n: 
        cnt += 1
        return
    bit[i] = 1
    printHello(i+1, n)
    bit[i] = 0
    printHello(i+1, n)

printHello(0, 3) # => cnt = 2^3(함수 호출 횟수)
```

```python
# 피보나치 수열
def fibo(n):
    if n < 2: 
        return n
    return fibo(n-1) + fibo(n-2)
# 중복 호출이 많기 때문에 n이 커질 수록 시간이 오래 걸림.
```



## 3. Memoization

* 이전에 계산한 값을 메모리에 저장해서 전체적인 실행속도를 빠르게 하는 기술

* 동적 계획법의 핵심이 되는 기술

* ```python
  # memo를 위한 배열을 할당하고, 모두 0으로 초기화 한다.
  # memo[0] = [0], memo[1]은 1로 초기화 한다.
  # 처음 함수를 호출하고 값을 저장함. 
  # memo에 값이 존재할 경우 함수 호출을 하지 않고 바로 값을 읽어옴.
  
  memo = [0] * 101
  def fibo(n):
      if n < 2: return n
      if memo[n] != 0:  # memo[n]이 0이 아닐 경우 값을 읽음
          return memo[n]
      else:  # 없다면 memo[n]에 값을 저장함.
          memo[n] = fibo(n-1) + fibo(n-2)
          return memo[n]
  
  print(fibo(40))
  ```

  

## 4. DP

* 최적화 문제를 해결하는 알고리즘
* 입력 크기가 작은 부분 문제들을 모두 해결한 후에 그 해들을 이용하여 보다 큰 크기의 부분 문제들을 해결하여 최종적으로 주어진 입력의 문제를 해결하는 알고리즘

#### 피보나치 수 DP 적용



## 5. DFS

