import sys
sys.stdin = open('BJ1890.txt')

N = int(input())
board = []
DP = [[0 for _ in range(N)] for _ in range(N)]
for i in range(N):
    board.append(list(map(int, input().split())))
DP[0][0] = 1
for i in range(N):
    for j in range(N):
        if i == N - 1 and j == N - 1:
            break
        if DP[i][j] > 0:
            if i + board[i][j] < N:
                DP[i + board[i][j]][j] += DP[i][j]
            if j + board[i][j] < N:
                DP[i][j + board[i][j]] += DP[i][j]
print(DP[N - 1][N - 1])