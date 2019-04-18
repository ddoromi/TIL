import sys
sys.stdin = open('1868.txt')

def poping(x, y):
    global count
    visit[x][y] = True
    XY = [[x - 1, y - 1], [x - 1, y], [x - 1, y + 1], [x, y + 1],
          [x + 1, y + 1], [x + 1, y], [x + 1, y - 1], [x, y - 1]]
    for xy in XY:
        if 0 <= xy[0] < N and 0 <= xy[1] < N and data[xy[0]][xy[1]] == '*':
            return
    data[x][y] = 0
    for xy in XY:
        if 0 <= xy[0] < N and 0 <= xy[1] < N and not visit[xy[0]][xy[1]]:
            poping(xy[0], xy[1])

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    data = []
    Min = N ** 2
    count = 0
    for i in range(N):
        data.append(list(input()))
    visit = [[False for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if data[i][j] == '.':
                poping(i, j)
                if data[i][j] == 0:
                    count += 1
    for i in range(N):
        for j in range(N):
            if data[i][j] == '.':
                XY = [[i - 1, j - 1], [i - 1, j], [i - 1, j + 1], [i, j + 1],
                      [i + 1, j + 1], [i + 1, j], [i + 1, j - 1], [i, j - 1]]
                for xy in XY:
                    if 0 <= xy[0] < N and 0 <= xy[1] < N:
                        if data[xy[0]][xy[1]] == 0:
                            break
                else:
                    count += 1
    print('#{} {}'.format(test_case, count))
