import sys
sys.stdin = open('BJ2667.txt')


def search(x, y):
    global count
    XY = [[x - 1, y], [x + 1, y], [x, y - 1], [x, y + 1]]
    MAP[x][y] = 0

    for dxy in XY:
        if MAP[dxy[0]][dxy[1]]:
            count += 1
            search(dxy[0], dxy[1])
        else:
            continue


N = int(input())
MAP = [[0 for _ in range(N + 2)]]
complex = []
complex_count = 0

for i in range(N):
    data = list(input())
    for j in range(N):
        data[j] = int(data[j])
    MAP.append([0] + data + [0])

MAP.append([0 for _ in range(N + 2)])

for i in range(1, N + 1):
    for j in range(1, N + 1):
        if MAP[i][j] == 1:
            count = 1
            complex_count += 1
            search(i, j)
            complex.append(count)

print(complex_count)
complex.sort()
for i in complex:
    print(i)



