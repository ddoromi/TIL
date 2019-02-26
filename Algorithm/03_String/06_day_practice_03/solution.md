##### solution

## 회문

```python
max_len = 0
for i in range(100):
    for j in range(100):
        # 길이가 짝수
        L, R, = i, j + 1
        cnt = 0
        
        while L >=0 and R < 100:
            if arr[i][L] == arr[i][R]
            	cnt += 2
            	L. R = L - 1, R + 1
            else:
           		break
        max_len = max(max_len, cnt)
        
        while L >=0 and R < 100:
            if arr[L][i] == arr[R][i]
            	cnt += 2
            	L, R = L - 1, R + 1
            else:
           		break
         max_len = max(max_len, cnt)
        
        # 길이가 홀수
        L, R, = j - 1, j + 1
        cnt = 1
        
        while L >=0 and R < 100:
            if arr[i][L] == arr[i][R]
            	cnt += 2
            	L. R = L - 1, R + 1
            else:
           		break
        max_len = max(max_len, cnt)
        
        while L >=0 and R < 100:
            if arr[L][j] == arr[R][j]
            	cnt += 2
            	L. R = L - 1, R + 1
            else:
           		break
         max_len = max(max_len, cnt)
```

```python
# 길이 = end - start + 1
# 반복 = 길이/2

max_len = 0
for row in range(100):
    for start in range(100):
        for end in range(99, start, -1):
            L = end - start + 1
            cnt = L // 2
            i = 0

            while i < cnt:
                if arr[row][start+i] != arr[row][end-i]: break
                i += 1
            if i == cnt:
                max_len = L
        
```



