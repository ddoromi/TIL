import sys
from collections import deque
sys.stdin = open('BJ2468.txt')

def search(x, y):
    XY = [[x, y - 1], [x, y + 1], [x - 1, y], [x + 1, y]]
    visit[x][y] = True
    for xy in XY:
        if xy[0] in [-1, N] or xy[1] in [-1, N]:
            continue
        if [xy[0], xy[1]] in check:
            if not visit[xy[0]][xy[1]]:
                search(xy[0], xy[1])

N = int(input())
MAP = []
height = deque()
check = deque()
Max = 0

for i in range(N):
    MAP.append(list(map(int, input().split())))

for i in range(N):
    for j in range(N):
        if MAP[i][j] not in height:
            height.append(MAP[i][j])

while len(height):
    H = height.popleft()
    visit = [[False for _ in range(N)] for _ in range(N)]
    count = 0
    for i in range(N):
        for j in range(N):
            if H < MAP[i][j]:
                check.append([i, j])

    while len(check):
        C = check.popleft()
        if not visit[C[0]][C[1]]:
            count += 1
            search(C[0], C[1])
    if Max < count:
        Max = count
    print(H, count)

