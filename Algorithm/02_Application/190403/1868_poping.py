import sys
sys.stdin = open('1868.txt')

# def poping(x, y):
#     global count
#     visit[x][y] = True
#     XY = [[x - 1, y - 1], [x - 1, y], [x - 1, y + 1], [x, y + 1],
#           [x + 1, y + 1], [x + 1, y], [x + 1, y - 1], [x, y - 1]]
#     for xy in XY:
#         if 0 <= xy[0] < N and 0 <= xy[1] < N and data[xy[0]][xy[1]] == '*':
#             return
#     data[x][y] = 0
#     for xy in XY:
#         if 0 <= xy[0] < N and 0 <= xy[1] < N and not visit[xy[0]][xy[1]]:
#             poping(xy[0], xy[1])
#
# T = int(input())
# for test_case in range(1, T + 1):
#     N = int(input())
#     data = []
#     Min = N ** 2
#     count = 0
#     for i in range(N):
#         data.append(list(input()))
#     visit = [[False for _ in range(N)] for _ in range(N)]
#     for i in range(N):
#         for j in range(N):
#             if data[i][j] == '.':
#                 poping(i, j)
#                 if data[i][j] == 0:
#                     count += 1
#     for i in range(N):
#         for j in range(N):
#             if data[i][j] == '.':
#                 XY = [[i - 1, j - 1], [i - 1, j], [i - 1, j + 1], [i, j + 1],
#                       [i + 1, j + 1], [i + 1, j], [i + 1, j - 1], [i, j - 1]]
#                 for xy in XY:
#                     if 0 <= xy[0] < N and 0 <= xy[1] < N:
#                         if data[xy[0]][xy[1]] == 0:
#                             break
#                 else:
#                     count += 1
#     print('#{} {}'.format(test_case, count))
for t in range(int(input())):
    size = int(input())
    board = [list(map(str, input())) for _ in range(size)]
    ans = 0

    drow = [-1, -1, 0, 1, 1, 1, 0, -1]
    dcol = [0, 1, 1, 1, 0, -1, -1, -1]
    for row in range(size):
        for col in range(size):
            if board[row][col] == "*":
                continue
            chk = False
            chk2 = False
            for idx in range(8):
                nrow, ncol = row + drow[idx], col + dcol[idx]
                if 0 <= nrow < size and 0 <= ncol < size:
                    if board[nrow][ncol] == "0":
                        chk = True
                    if board[nrow][ncol] == "*":
                        chk2 = True
            if chk and not chk2:
                board[row][col] = "0"
            elif not chk and not chk2:
                ans += 1
    for row in range(size):
        for col in range(size):
            cnt = 0
            if board[row][col] == ".":
                for idx in range(8):
                    nrow, ncol = row + drow[idx], col + dcol[idx]
                    if 0 <= nrow < size and 0 <= ncol < size and board[nrow][ncol] == "0":
                        break
                else:
                    ans += 1

    print(f"#{t + 1} {ans}")