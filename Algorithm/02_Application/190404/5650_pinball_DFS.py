import sys
sys.stdin = open('5650.txt')
sys.setrecursionlimit(0xfffff)

def start(sx, sy, now_x, now_y):
    global Max
    XY = [[now_x - 1, now_y], [now_x + 1, now_y], [now_x, now_y - 1], [now_x, now_y + 1]]
    for i in range(4):
        pinball(sx, sy, XY[i][0], XY[i][1], i, 0)
        Max = max(Max, score)
    return

# 상: 0, 하: 1, 좌: 2, 우: 3
def pinball(sx, sy, x, y, direction, count):
    global score
    if (x == sx and y == sy) or (0 <= x < N and 0 <= y < N and board[x][y] == -1):
        score = count
        return
    # 상
    if direction == 0:
        if x < 0 or board[x][y] in [1, 4, 5]:
            pinball(sx, sy, x + 1, y, 1, count + 1)
        elif board[x][y] == 2:
            pinball(sx, sy, x, y + 1, 3, count + 1)
        elif board[x][y] == 3:
            pinball(sx, sy, x, y - 1, 2, count + 1)
        elif 6 <= board[x][y] < 11:
            for hh in hole[board[x][y] - 6]:
                if hh != [x, y]:
                    pinball(sx, sy, hh[0] - 1, hh[1], direction, count)
        else:
            pinball(sx, sy, x - 1, y, direction, count)
    # 하
    elif direction == 1:
        if x >= N or board[x][y] in [2, 3, 5]:
            pinball(sx, sy, x - 1, y, 0, count + 1)
        elif board[x][y] == 1:
            pinball(sx, sy, x, y + 1, 3, count + 1)
        elif board[x][y] == 4:
            pinball(sx, sy, x, y - 1, 2, count + 1)
        elif 6 <= board[x][y] < 11:
            for hh in hole[board[x][y] - 6]:
                if hh != [x, y]:
                    pinball(sx, sy, hh[0] + 1, hh[1], direction, count)
        else:
            pinball(sx, sy, x + 1, y, direction, count)
    # 좌
    elif direction == 2:
        if y < 0 or board[x][y] in [3, 4, 5]:
            pinball(sx, sy, x, y + 1, 3, count + 1)
        elif board[x][y] == 1:
            pinball(sx, sy, x - 1, y, 0, count + 1)
        elif board[x][y] == 2:
            pinball(sx, sy, x + 1, y, 1, count + 1)
        elif 6 <= board[x][y] < 11:
            for hh in hole[board[x][y] - 6]:
                if hh != [x, y]:
                    pinball(sx, sy, hh[0], hh[1] - 1, direction, count)
        else:
            pinball(sx, sy, x, y - 1, direction, count)
    # 우
    elif direction == 3:
        if y == N or board[x][y] in [1, 2, 5]:
            pinball(sx, sy, x, y - 1, 2, count + 1)
        elif board[x][y] == 4:
            pinball(sx, sy, x - 1, y, 0, count + 1)
        elif board[x][y] == 3:
            pinball(sx, sy, x + 1, y, 1, count + 1)
        elif 6 <= board[x][y] < 11:
            for hh in hole[board[x][y] - 6]:
                if hh != [x, y]:
                    pinball(sx, sy, hh[0], hh[1] + 1, direction, count)
        else:
            pinball(sx, sy, x, y + 1, direction, count)

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    board = []
    Max = 0
    hole = [[] for _ in range(5)]
    for i in range(N):
        board.append(list(map(int, input().split())))
    for i in range(N):
        for j in range(N):
            if 6 <= board[i][j] < 11:
                hole[board[i][j] - 6].append([i, j])
    for i in range(N):
        for j in range(N):
            if board[i][j] == 0:
                score = 0
                start(i, j, i, j)

    print('#{} {}'.format(test_case, Max))