```python
arr= 'ABCDE0'
N = len(arr)
R = 3
pick = [0] * R

def comb(k, start):
    if k == R:
        print(arr[pick[0]], arr[pick[1], arr[pick[2]]])
        return
    for i in range(start, N)
    pick[k] = i
    comb (k + 1, i + 1)
comb(0, 0)

```

