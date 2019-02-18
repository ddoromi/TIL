# 02_day [190218]



## 2. 배열 2(Array 2)

### 배열 : 2차 배열









### 부분집합 생성

#### 1. 부분집합 생성하기

* 부분집합의 수 : 2^(원소의 개수)

* 코드 특성 상 재귀함수를 만들어서 사용함.

  ```python
  arr = [1, 3, 5]
  bit = [0] * len(arr)
  
  for i in [0, 1]:
      bit[0] = i
      for j in [0, 1]:
          bit[1] = j
      for k in [0, 1]:
          bit[2] = k
          print(bit)
         
  ```

* ```python
  # 부분집합 합 구하기
  arr = [1, 2, 3, 5, 6, 7, 8, 9, 10]
  
  n = len(arr)
  
  for i in range(1 << n): # 0 ~ 63
      result = 0
  
      # 2^0 ~ 2^5에 해당하는 비트 값을 확인
      for j in range(n):
          if i & (1 << j) != 0:
              result += arr[j]
              # print(arr[j], end='')
  
      if result == 10:
          for j in range(n):
              if i & (1 << j) != 0:
                  print(arr[j], end='')
          print()
  ```

  

### 바이너리 서치

#### 1. 비트 연산자 

* 장점 : 메모리를 적게 사용함, 실행 속도가 빠름.
* 단점 : 가독성이 떨어짐.
* 1 byte = 8bit

##### & 연산자

- 비트 단위로 AND 연산을 함.

- i & (1<<j) : j의 j번째 비트가 1인지 아닌지 리턴.

- ```python
  n = 19
  if n % 2 == 1:
      return '홀수'
  if n & 1 == 0:
      return '홀수'
  ```

##### | 연산자

- 비트 단위로 OR 연산을 함.

##### << 연산자

- 피연산자의 비트 열을 왼쪽으로 이동시킴.
- 오른쪽 끝의 빈자리는 0으로 채움.
- == *2 

##### >> 연산자

- 피연산자의 비트 열을 오른쪽으로 이동시킴.
- 왼쪽 끝의 빈자리는 0으로 채움.
- == / 2 => 0.5는 버려짐.



#### 2. 검색

* 종류
  * 순차 검색 : O(n), n의 크기가 클 경우 사용하지 않음.
  * 이진 검색 : O(log(n))
  * 해쉬 : O(1), 공간복잡도가 커짐.

##### 순차 검색 (O(n))

* 정렬되어 있지 않은 경우
  - 첫 번째 원소부터 차례대로 검색 
  - 찾으면 인덱스 반환, 찾지 못하면 검색 실패
* 정렬된 경우
  * 원소의 키 값이 검색 대상의 키 값보다 크면 찾는 원소가 없다는 것이므로 더 이상 검색하지 않고 검색을 종료함.

##### 이진 검색

* 찾을 때까지 이진 검색을 순환적으로 반복 수행함으로써 검색 범위를 반으로 줄여가면서 보다 빠르게 검색을 수행함.
* 자료가 정렬되어 있는 상태여야 함.
* 검색과정
  * 자료의 중앙에 있는 원소와 목표 값을 비교함.
  * 목표 값이 작으면 중앙의 왼쪽에서 다시 검색을 수행하고, 크면 중앙의 오른쪽에서 다시 검색을 수행함.
  * 찾을 때까지 과정 반복

* ```python
  arr = [2, 5, 7, 8, 12, 16, 21, 23, 33, 39, 42, 45, 45, 49, 62, 88]
  
  def binarySearch(arr, key):
      start, end = 0, len(arr)-1
  
      while start <= end:
          mid = (start + end) >> 1
  
          if arr[mid] == key:
              return mid
          elif arr[mid] > key:
              end = mid - 1
          else:
              start = mid + 1
  
      # 못 찾았을 때
      return -1
  ```

* ```python
  # 재귀함수
  def binary_search(arr, start, end, key):
      if start > end:
          return -1
      
      mid = (start + end) >> 1
      if arr[mid] == key:
          return mid
      elif arr[mid] > key:
          return binary_search(arr, start, mid-1, key)
      else:
          return binary_search(arr, key, mid+1, end)
  ```

##### 인덱스

* 키-필드만 가짐 => 테이블을 저장하는데 필요한 디스크 공간보다 작음.



### 셀렉션 알고리즘

* 저장되어 있는 자료로부터 K번째로 큰/작은 원소를 찾는 방법

* ```python
  arr = [64, 25, 10, 22, 11]
  
  N = len(arr)
  
  for i in range(N-1):
      minIdx = i
      
      for j in range(minIdx+1, N):
          if arr[minIdx] > arr[j]: 
              minIdx = j
      
      arr[i], arr[minIdx] = arr[minIdx], arr[i]
  
  print(arr)
  ```

### 선택 정렬