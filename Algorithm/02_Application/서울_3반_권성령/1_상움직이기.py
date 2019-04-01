import sys
from collections import deque
sys.stdin = open('1.txt')

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    X, Y, TX, TY = map(int, input().split())
    MAP = [[0 for _ in range(N)] for _ in range(N)]
    MAP[X][Y] = 1
    route = deque()
    count = deque()
    route.append([X, Y])
    count.append(0)
    while len(route):
        X, Y = route.popleft()
        d = count.popleft()
        if X == TX and Y == TY:
            result = d
            break
        XY = [[X - 3, Y - 2], [X - 3, Y + 2], [X - 2, Y + 3], [X + 2, Y + 3],
              [X + 3, Y + 2], [X + 3, Y - 2], [X + 2, Y - 3], [X - 2, Y - 3]]
        for xy in XY:
            if 0 <= xy[0] <= N - 1 and 0 <= xy[1] <= N - 1:
                route.append([xy[0], xy[1]])
                count.append(d + 1)
    print('#{} {}'.format(test_case, result))