import sys
from collections import deque
sys.stdin = open('BJ7576.txt')

N, M = map(int, input().split())
tomato = deque()
mute = deque()
day = deque()
tomato.append([-1 for _ in range(N + 2)])

for i in range(M):
    tomato.append([-1] + list(map(int, input().split())) + [-1])
tomato.append([-1 for _ in range(N + 2)])

for i in range(1, M + 1):
    for j in range(1, N + 1):
        if tomato[i][j] == 1:
            mute.append([i, j])
            day.append(0)

while len(mute):
    T = mute.popleft()
    D = day.popleft()
    XY = [[T[0], T[1] - 1], [T[0], T[1] + 1], [T[0] - 1, T[1]], [T[0] + 1, T[1]]]
    for xy in XY:
        if tomato[xy[0]][xy[1]] == 0:
            tomato[xy[0]][xy[1]] = 1
            mute.append([xy[0], xy[1]])
            day.append(D + 1)

for i in range(1, M + 1):
    for j in range(1, N + 1):
        if tomato[i][j] == 0:
            D = -1
            break
print(D)
