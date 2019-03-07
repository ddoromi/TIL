import sys
sys.stdin = open('04.txt')

T = int(input())
for test_case in range(T):
    N, M = map(int, input().split())
    board = [[0 for _ in range(N+1)] for _ in range(N+1)]
    board[N//2][N//2], board[N//2+1][N//2+1] = 2, 2
    board[N//2][N//2+1], board[N//2+1][N//2] = 1, 1
    players = []

    for m in range(M):
        players.append(list(map(int, input().split())))

    for player in players:
        board[player[0]][player[1]] = player[2]
        print(player)

        # 위
        i = 1
        while player[1] - i > 0:
            if player[2] == board[player[0]][player[1] - i]:
                for j in range(1, i):
                    board[player[0]][player[1] - i] = player[2]
                break
            elif (board[player[0]][player[1] - i] != 0) and (player[2] != board[player[0]][player[1] - i]):
                i += 1
            else:
                break

        # 아래
        i = 1
        while player[1] + i <= N:
            if player[2] == board[player[0]][player[1] + i]:
                for j in range(1, i):
                    board[player[0]][player[1] + i] = player[2]
                break
            elif (board[player[0]][player[1] + i] != 0) and (player[2] != board[player[0]][player[1] + i]):
                i += 1
            else:
                break

        # 왼쪽
        i = 1
        while player[0] - i > 0:
            if player[2] == board[player[0] - i][player[1]]:
                for j in range(1, i):
                    board[player[0] - i][player[1]] = player[2]
                break
            elif (board[player[0] - i][player[1]] != 0) and (player[2] != board[player[0] - i][player[1]]):
                i += 1
            else:
                break

        # 오른쪽
        i = 1
        while player[0] + i <= N:
            if player[2] == board[player[0] + i][player[1]]:
                for j in range(1, i):
                    board[player[0] + i][player[1]] = player[2]
                break
            elif (board[player[0] + i][player[1]] != 0) and (player[2] != board[player[0] + i][player[1]]):
                i += 1
            else:
                break

        # 오른쪽 위 대각선
        i = 1
        while (player[0] + i <= N) and (player[1] - i > 0):
            if player[2] == board[player[0] + i][player[1] - i]:
                for j in range(1, i):
                    board[player[0] + i][player[1] - i] = player[2]
                break
            elif (board[player[0] + i][player[1] - i] != 0) and (player[2] != board[player[0] + i][player[1] - i]):
                i += 1
            else:
                break

        # 왼쪽 위 대각선

        i = 1
        while (player[0] - i > 0) and (player[1] - i > 0):
            if player[2] == board[player[0] - i][player[1] - i]:
                for j in range(1, i):
                    board[player[0] - i][player[1] - i] = player[2]
                break
            elif (board[player[0] - i][player[1] - i] != 0) and (player[2] != board[player[0] - i][player[1] - i]):
                i += 1
            else:
                break

        # 오른쪽 아래 대각선
        i = 1
        while player[0] + i <= N and player[1] + i <= N:
            if player[2] == board[player[0] + i][player[1] + i]:
                for j in range(1, i):
                    board[player[0] + i][player[1] + i] = player[2]
                break
            elif (board[player[0] + i][player[1] + i] != 0) and (player[2] != board[player[0] + i][player[1] + i]):
                i += 1
            else:
                break

        # 왼쪽 아래 대각선
        i = 1
        while player[0] - i > 0 and player[1] + i <= N:
            if player[2] == board[player[0] - i][player[1] + i]:
                for j in range(1, i):
                    board[player[0] - i][player[1] + i] = player[2]
                break
            elif (board[player[0] - i][player[1] + i] != 0) and (player[2] != board[player[0] - i][player[1] + i]):
                i += 1
            else:
                break

    w_count, b_count = 0, 0
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if board[i][j] == 1:
                b_count += 1
            elif board[i][j] == 2:
                w_count += 1

    print('#{} {} {}'.format(test_case + 1, b_count, w_count))