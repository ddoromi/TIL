### 4837_부분집합

```python
for test_case in range(1, T+1):
    N, K = map(int, input().split())
    ans = 0
    
    for subset in range(1 << 12):
        cnt = 0 # 1의 개수
       	Sum = 0 # 원소의 합
        for i in range(2):
            if subset & (1<<i) != 0:
                # 1의 개수 카운팅
                cnt += 1
                Sum += i + 1
```

### 이게 뭐야ㅠㅠ

``` python
arr = 'ABCD'
N = len(arr)

for subset in range(1<<N):
    cntA = cntB = 0
    for i in range(N):
        if subset & (1<<i): cntA += 1
        else: cntB += 1
    
    A, B = [], []
    if cntA == cntB:
        for i in range(N):
            if subset & (1<<i): A.append(arr[i])
            else: B.append(arr[i])
        print(A, B)
```

### 4839_이진탐색

```python

```

### 4843_특별한 정렬

```python
for test_case in range(T):
	N = int(input())
    arr = list(map(int, input().split()))
    
    for i in range(10):
        idx = i
        if i & 1:
            for j in range(1+i, N):
                if arr[idx] > arr[j]:
                    idx = j
        else:
            for j in range(i+1, N):
                if arr[idx] < arr[j]:
                    idx = j        
```

### 1259_금속막대

```python
# 파이썬
N = int(input())
arr = list(map(int, input().split()))
bars = []

for i in range(N):
    bars.append(arr[i*2], arr[i*2+1])
ans = 
```

```c
# C
N = int(input())
arr = list(map(int, input().split()))
```









