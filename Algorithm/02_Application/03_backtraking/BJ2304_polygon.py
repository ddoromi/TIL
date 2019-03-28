import sys
sys.stdin = open('2304.txt')

N = int(input())
data = []
max_height = 0

for i in range(N):
    data.append(list(map(int, input().split())))

for i in range(N):
    Min = data[i][0]
    index = i
    for j in range(i + 1, N):
        if Min > data[j][0]:
            Min = data[j][0]
            index = j
    data[i], data[index] = data[index], data[i]

for i in range(N):
    if max_height < data[i][1]:
        max_height, max_index = data[i][1], data[i][0]

h = data[0][1]
area = 0

for i in range(1, N):
    if data[i][0] <= max_index:
        area += (data[i][0] - data[i - 1][0]) * h
        if data[i][1] > h:
            h = data[i][1]

h2 = data[-1][1]
for i in range(N - 2, -1, -1):
    if data[i][0] >= max_index:
        area += (data[i + 1][0] - data[i][0]) * h2
        if data[i][1] > h2:
            h2 = data[i][1]
print(area + max_height)


