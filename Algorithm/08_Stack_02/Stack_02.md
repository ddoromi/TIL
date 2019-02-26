##### [2019. 02. 06]

# 5. Stack_02

### 계산기

* 문자열로 된 계산식이 주어질 때, 스택을 이용하여 값을 계산할 수 있음.

* 문자열 수식 계산의 일반적인 방법

  step1. 중위 표기법(연산자를 피연산자 가운데 표기)의 수식을 후위 표기법으로 변경(스택 이용)

  step2. 후위 표기법(연산자를 피연산자 뒤 표기)의 수식을 스택을 이용하여 계산

  

### 백트래킹

* 해를 찾는 도중에 막히면(해가 아니면) 되돌아가서 다시 해를 찾는 기법

* 최적화 문제와 결정 문제를 해결할 수 있음

  * 결정 문제: 문제의 조건을 만족하는 해가 존재하는지의 여부를 답하는 문제

    (미로 찾기, n-Queen 문제, Map coloring, 부분 집합의 합 문제 등)

* 부분집합 구하기

  ``` python
  bits = [0] * 3
  def subset(k, n):
      if k == n:
          print(bits)
      else:
          bits[k] = 0
          subset(k + 1, n)
          bits[k] = 1
          subset(k + 1, n)
          
   subset(0, 3)
  ```

* 조합

  ```python
  arr = 'ABC'
  N = len(arr)
  for i in range(N):
      for j in range(N):
          if i == j: continue
          for k in range(N):
              if k == i or k == j: continue
              print(arr[i], arr[j], arr[k])
              
  # 재귀
  arr = 'ABC'
  N = len(arr)
  order = [0] * N
  
  def perm(k, n):
      if k == n:
          # order[] 저장된 순서를 확인
          return
      visit = [False] * N
      for i in range(k):
          visit[order[i]] True
      for i in range(n):
          if visit[i]: continue
          order[k] = i
          perm(k + 1, n)
          
  perm(0, 3)  # 3: 요소 수
  
  
  # bit 사용
  arr = 'ABC'
  N = len(arr)
  order = [0] * N
  
  def perm(k, n, visit):
      if k == n:
          # order[] 저장된 순서를 확인
          return
  
      for i in range(n):
          if visit & (1 << i): continue
          order[k] = i
          perm(k + 1, n, visit | (1 << j))
          
  perm(0, N, 0)  # 3: 요소 수
  ```

  

### 분할정복

ㅅ



### 실습