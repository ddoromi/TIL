import sys
sys.stdin = open('1953.txt')
from collections import deque

T = int(input())
for test_case in range(1, T + 1):
    N, M, R, C, L = map(int, input().split())
    MAP = []
    for i in range(N):
        MAP.append(list(map(int, input().split())))
    possible = [[1, 2, 5, 6], [1, 2, 4, 7], [1, 3, 4, 5], [1, 3, 6, 7]]
    pipe = [[], [0, 1, 2, 3], [0, 1], [2, 3], [0, 3], [1, 3], [1, 2], [0, 2]]
    criminal = deque([[R, C]])
    distance = deque()
    distance.append(1)
    count = 1
    visit = [[False for _ in range(M)] for _ in range(N)]
    while criminal:
        X, Y = criminal.popleft()
        d = distance.popleft()
        if d == L:
            break
        visit[X][Y] = True
        XY = [[X - 1, Y], [X + 1, Y], [X, Y - 1], [X, Y + 1]]
        for ii in pipe[MAP[X][Y]]:
            if XY[ii][0] in [-1, N] or XY[ii][1] in [-1, M] or visit[XY[ii][0]][XY[ii][1]]:
                continue
            if MAP[XY[ii][0]][XY[ii][1]] in possible[ii]:
                count += 1
                criminal.append([XY[ii][0], XY[ii][1]])
                distance.append(d + 1)
    print('#{} {}'.format(test_case, count))