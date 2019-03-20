import sys
sys.stdin = open('BJ17070.txt')

for test_case in range(4):
    count = 0
    N = int(input())
    floor = []
    right = [[0 for _ in range(N)] for _ in range(N)]
    down = [[0 for _ in range(N)] for _ in range(N)]
    cross = [[0 for _ in range(N)] for _ in range(N)]

    for i in range(N):
        floor.append(list(map(int, input().split())))

    right[0][1] = 1
    for i in range(N):
        for j in range(1, N):
            if i == 0 and j == 1:
                continue
            if floor[i][j] == 0:
                if j == 1 and i > 0:
                    continue
                if i == 0:
                    right[i][j] = right[i][j - 1]
                    continue
                if j == N - 1:
                    down[i][j] = cross[i - 1][j] + down[i - 1][j]
                    if floor[i - 1][j] == 0 and floor[i][j - 1] == 0:
                        cross[i][j] = right[i - 1][j - 1] + down[i - 1][j - 1] + cross[i - 1][j - 1]
                    continue
                if i == N - 1:
                    right[i][j] = cross[i][j - 1] + right[i][j - 1]
                    if floor[i - 1][j] == 0 and floor[i][j - 1] == 0:
                        cross[i][j] = right[i - 1][j - 1] + down[i - 1][j - 1] + cross[i - 1][j - 1]
                    continue
                right[i][j] = cross[i][j - 1] + right[i][j - 1]
                down[i][j] = cross[i - 1][j] + down[i - 1][j]
                if floor[i - 1][j] == 0 and floor[i][j - 1] == 0:
                    cross[i][j] = right[i - 1][j - 1] + down[i - 1][j - 1] + cross[i - 1][j - 1]
    print(right)
    print(down)
    print(cross)
    print(right[N - 1][N - 1] + down[N - 1][N - 1] + cross[N - 1][N - 1])