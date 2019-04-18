import sys
sys.stdin = open('1953.txt')
from collections import deque

T = int(input())
for test_case in range(1, T + 1):
    N, M, R, C, L = map(int, input().split())
    MAP = []
    cnt = 1
    for i in range(N):
        MAP.append(list(map(int, input().split())))
    possible = [[1, 2, 5, 6], [1, 2, 4, 7], [1, 3, 4, 5], [1, 3, 6, 7]]
    pipe = [[], [0, 1, 2, 3], [0, 1], [2, 3], [0, 3], [1, 3], [1, 2], [0, 2]]
    criminal, distance = deque([[R, C]]), deque([1])
    count = 1
    visit = [[0 for _ in range(M)] for _ in range(N)]
    visit[R][C] = 1
    while len(criminal):
        X, Y = criminal.popleft()
        if visit[X][Y] == L:
            break
        XY = [[X - 1, Y], [X + 1, Y], [X, Y - 1], [X, Y + 1]]
        for ii in pipe[MAP[X][Y]]:
            if XY[ii][0] in [-1, N] or XY[ii][1] in [-1, M] or visit[XY[ii][0]][XY[ii][1]] > 0:
                continue
            if MAP[XY[ii][0]][XY[ii][1]] in possible[ii]:
                criminal.append([XY[ii][0], XY[ii][1]])
                visit[XY[ii][0]][XY[ii][1]] = visit[X][Y] + 1
                cnt += 1
    print('#{} {}'.format(test_case, cnt))