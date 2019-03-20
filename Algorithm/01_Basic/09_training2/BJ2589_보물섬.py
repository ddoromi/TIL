import sys
from collections import deque
sys.stdin = open('BJ2589.txt')

N, M = map(int, input().split())
MAP = [['W' for _ in range(M + 2)]]
for i in range(N):
    MAP.append(['W'] + list(input()) + ['W'])
MAP.append(['W' for _ in range(M + 2)])

ground = deque()
distance = deque()
Max = 0
for i in range(1, N + 1):
    for j in range(1, M + 1):
        if MAP[i][j] == 'L':
            visit = [[False for _ in range(M + 1)] for _ in range(N + 1)]
            ground.append([i, j])
            distance.append(0)
            while len(ground):
                g = ground.popleft()
                d = distance.popleft()
                XY = [[g[0] - 1, g[1]], [g[0] + 1, g[1]], [g[0], g[1] - 1], [g[0], g[1] + 1]]
                for xy in XY:
                    if MAP[xy[0]][xy[1]] == 'L':
                        if not visit[xy[0]][xy[1]]:
                            visit[xy[0]][xy[1]] = True
                            ground.append([xy[0], xy[1]])
                            distance.append(d + 1)

            if Max < d:
                Max = d
print(Max)
