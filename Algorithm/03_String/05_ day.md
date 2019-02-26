##### 05_ day  [19. 02. 20]

# 3. 문자열(String)

### 1. 문자열

#### 1. 문자열 복사

```python
str1 = 'abcde'
str2 = str1
print(id(str1), id(str2)) # 같음

str2 = str2 + 'x'
print(id(str1), id(str2)) # str2는 새로운 주소를 가짐 => immutable
```

```python
List1 = [0, 1, 2, 3]
List2 = List1
print(List1, List2) # 같은 값을 가짐 => mutable
```

#### 2. C/ java, python 문자열 처리 차이

##### 1. C 

- 아스키 코드로 저장함
- 한글은 2byte를 차지함.

##### 2. java/ python

- 유니코드로 저장하기 때문에 한글과 영어의 크기 차이가 없음.

#### 3. 문자열 뒤집기

```python
str = list('algorithm')
cnt = len(str)//2

# 뒤집는 로직
for i in range(cnt):
    str[i], str[len(str)-1] = str[len(str)-1-i], str[i]
print(str)

# for문보다 모듈 사용할 것
print('algorithm'[::-1]) # 뒤집어진 상태로 출력됨
```

```python
# 팰린드롬
str = 'abcddcba'
cnt = len(str)//2
isPalindrome = True

for i in range(cnt):
    if str[i] != str[len(str)-1-i]:
        isPalindrome = False
        break
print(isPalindrome)
```

####  4. 문자열 비교

##### 1. 문자열 대소

- 사전 순으로 비교함
- 부등호 사용 ( A < B ) => A가 사전 순으로 먼저 옴.

#### 5. 문자열 숫자를 정수로 변환하기

* C : atoi() <=> itoa()
* java : parse() <=> toString()
* python : int(' ')

#### 연습문제

* 정수를 문자열로 바꾸기

* ```python
  num = 12345
  result = ''
  
  while num !=0 :
      result += str(num%10)
      num = num // 10
  
  print(result[::-1])
  ```



## 2. 패턴매칭

* 텍스트 : t , 길이는 n, 위치는 i
* 패턴 : p, 길이는 m, 위치는 j

#### 1. 고지식한 패턴 검색 알고리즘(Brute Force)

* 최악의 경우 모든 경우를 비교하고 검색에 실패함.

* ```python
  p = 'CATTCCCTGCGCCGC'
  t = 'ATTTGTGCATGTTTGAGGTTTTACACGTACGTACGAGAAACTGAACGTACCTACCTACGACATTCCCTGCGCGCCGCCATA'
  n, m = len(t), len(p)
  i = j = 0
  
  while i < n:    
      # 값이 같다면 위치를 하나씩 증가시켜서 비교함
      if t[i] == p[j]:
          i , j = i + 1, j + 1
          # p의 길이만큼 비교가 끝났을 때
      	if j == m:
              print(t[i-j:i])
              break   
      # 다르면 i는 원래 위치의 다음 위치, j는 원점으로 돌림
      else:
          i = i - j + 1
          j = 0
  ```

* ```python
  p = 'is'
  t = 'This is a book~!'
  M = len(p)
  N = len(t)
  
  def BruteForce(p, t):
      i = 0  # t의 인덱스
      j = 0  # p의 인덱스
      
      while j < M and i < N:
          if t[i] != p[j]:
              i = i - j  # 원래 자리 위치로 바꿈
              j = -1
          i = i + 1  # 원래 자리의 다음 위치
          j = j + 1  # if문을 만나고 난 뒤에는 j = 0
      if j == M:
          return i - M  # 검색성공
      else:
          return -1  # 검색실패
  ```

#### 2. KMP 알고리즘

* 패턴을 전처리하여 배열을 구해서 잘못된 시작을 최소화함.
* brute force 과정에서 불필요한 과정을 제외함.
* j를 어디로 바꿀지 계산함 => 항상 0이 아님
* i를 절대 앞으로 돌리지 않음 => 제자리거나 뒤로 전진함.
* 문자열 크기에 상관 없이 효율성이 일정함.

##### 1. 과정

* 실패한 위치의 전 패턴은 공통적으로 가지고 있음. => 계산해서 불필요한 작업을 건너뜀

* 공통된 i의 접미어와 j의 접두어를 계산함.

* i는 제자리에 두고 j의 위치는 j의 접두어 다음 위치로 바꾸어 비교함.

* ```python
  p = 'abcdabcef'                                                                       # pattern
  t = 'alksdabcdabcflaskjflkabcdjsaflkjasdkdsajfabcdabceflksadjabcdaksfjffsdaf'      # text
  
  
  m, n = len(p), len(t)
  next = [0] * (m + 1)
  
  # 전처리
  next[0] = -1 # j에 +1을 해서 0으로 만들기 위해
  # i가 앞서가고 j가 뒤따라감
  i, j = 0, -1
  
  while i < m:
      while j >= 0 and p[j] != p[i]:
          j = next[j]
          
      i, j = i + 1, j + 1
      next[i] = j
  
  print(next)
  
  # 매칭
  i = j = 0
  while i < n:
      while j >= 0 and p[j] != t[i]:
          j = next[j]
  
      i, j = i + 1, j + 1
  
      if j == m:
          print(t[i - j:])
          break
  ```

#### 3. 해시

```python
p = 'abcdabcef'                                                                      
t = 'alksdabcdabcflaskjflkabcdjsaflkjasdkdsajfabcdabceflksadjabcdaksfjffsdaf'
n, m = len(t), len(p)

th, ph, h0 = 0, 0, 1
for i in range(m):
    th = (th * 10 + ord(t[i])) & 12345
    ph = (ph * 10 + ord(p[i])) & 12345

for i in range(m-1):
    h0 = (h0*10) % 12345
    
for i in range(n-m+1):
    if ph == th:
        j = 0
        while j < m:
            if t[i+j] != p[j]: break
            j += 1
        if j == m:
            print(t[i:])
    th = ((th - ord(t[i])) * 10 + ord(t[i+m])) % 12345 
```

#### 4. 보이어-무어 알고리즘

* 문자열이 클 경우 효율성이 감소됨.
* 패턴의 오른쪽 끝에 있는 문자가 불일치 하고 이 문자가 패턴 내에 존재하지 않는 경우 패턴의 길이 만큼 이동함. 







## 3. 문자열 암호화





## 4. 문자열 압축





