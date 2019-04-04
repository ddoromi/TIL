import sys
sys.stdin = open('BJ2437.txt')

N = int(input())
data = list(map(int, input().split()))
data.sort()
result = 0

if data[0] != 1:
    result = 1
if result == 0 and len(data) == 2:
    if data[1] > 2:
        result = 2
if result == 0:
    check = False
    while len(data) > 1:
        a, b = data.pop(0), data[0]
        if b > a + 1:
            result = a + 1
            check = True
            break
        else:
            data[0] = a + b
    if not check:
        result = data[0] + 1
print(result)