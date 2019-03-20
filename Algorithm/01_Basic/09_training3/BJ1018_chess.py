import sys
sys.stdin = open('BJ1018.txt')

for test_case in range(2):
    N, M = map(int, input().split())
    board = []
    Min = 2000
    chess_w = [['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
               ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
               ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
               ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
               ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
               ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
               ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
               ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W']]
    chess_b = [['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
               ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
               ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
               ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
               ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
               ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
               ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
               ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B']]

    for i in range(N):
        board.append(list(input()))

    for i in range(N - 7):
        for j in range(M - 7):
            count_w = count_b = 0
            for k in range(8):
                for l in range(8):
                    if board[i + k][j + l] != chess_w[k][l]:
                        count_w += 1
                    if board[i + k][j + l] != chess_b[k][l]:
                        count_b += 1
            Min = min(count_w, count_b, Min)
    print(Min)