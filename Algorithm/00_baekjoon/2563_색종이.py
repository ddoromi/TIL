N = int(input())
data = [[0 for _ in range(101)] for _ in range(101)]
count = 0

for i in range(N):
    x, y = map(int, input().split())
    for j in range(10):
        for k in range(10):
            data[y+j][x+k] = 1

for i in range(101):
    for j in range(101):
        if data[i][j] == 1:
            count += 1

print(count)