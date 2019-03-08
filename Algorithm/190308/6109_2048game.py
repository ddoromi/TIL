import sys
sys.stdin = open('6109.txt')

T = int(input())
for test_case in range(T):
    N, S = input().split()
    board = []
    N = int(N)
    check = True
    for i in range(N):
        board.append(list(map(int, input().split())))


    stack = [[] for _ in range(N)]

    if S == 'up' or S == 'down':

        for i in range(N):
            for j in range(N):
                if board[j][i] > 0:
                    stack[i].append(board[j][i])

        if S == 'up':
            for i in range(N):
                for j in range(N):
                    if len(stack[i]) > 0:
                        board[j][i] = stack[i].pop(0)
                    else:
                        board[j][i] = 0
        else:
            for i in range(N):
                for j in range(N-1, -1, -1):
                    if len(stack[i]) > 0:
                        board[j][i] = stack[i].pop(-1)
                    else:
                        board[j][i] = 0

        stack = [[] for _ in range(N)]
        for i in range(N):
            if S == 'up':
                for j in range(1, N):
                    if board[j][i] != 0 and board[j][i] == board[j-1][i]:
                        board[j-1][i] *= 2
                        board[j][i] = 0
            else:
                for j in range(N-1):
                    if board[j][i] != 0 and board[j][i] == board[j+1][i]:
                        board[j+1][i] *= 2
                        board[j][i] = 0

        stack = [[] for _ in range(N)]
        for i in range(N):
            for j in range(N):
                if board[j][i] > 0:
                    stack[i].append(board[j][i])

        if S == 'up':
            for i in range(N):
                for j in range(N):
                    if len(stack[i]) > 0:
                        board[j][i] = stack[i].pop(0)
                    else:
                        board[j][i] = 0
        else:
            for i in range(N):
                for j in range(N-1, -1, -1):
                    if len(stack[i]) > 0:
                        board[j][i] = stack[i].pop(-1)
                    else:
                        board[j][i] = 0

    else:
        for i in range(N):
            for j in range(N):
                if board[i][j] > 0:
                    stack[i].append(board[i][j])

        if S == 'left':
            for i in range(N):
                for j in range(N):
                    if len(stack[i]) > 0:
                        board[i][j] = stack[i].pop(0)
                    else:
                        board[i][j] = 0
        else:
            for i in range(N):
                for j in range(N-1, -1, -1):
                    if len(stack[i]) > 0:
                        board[i][j] = stack[i].pop(-1)
                    else:
                        board[i][j] = 0

        stack = [[] for _ in range(N)]
        for i in range(N):
            if S == 'right':
                for j in range(N-1):
                    if board[i][j] != 0 and board[i][j] == board[i][j+1]:
                        board[i][j+1] *= 2
                        board[i][j] = 0
            else:
                for j in range(1, N):
                    if board[i][j] != 0 and board[i][j] == board[i][j-1]:
                        board[i][j-1] *= 2

                        board[i][j] = 0
        stack = [[] for _ in range(N)]
        for i in range(N):
            for j in range(N):
                if board[i][j] > 0:
                    stack[i].append(board[i][j])

        if S == 'left':
            for i in range(N):
                for j in range(N):
                    if len(stack[i]) > 0:
                        board[i][j] = stack[i].pop(0)
                    else:
                        board[i][j] = 0
        else:
            for i in range(N):
                for j in range(N-1, -1, -1):
                    if len(stack[i]) > 0:
                        board[i][j] = stack[i].pop(-1)
                    else:
                        board[i][j] = 0

    print('#{}'.format(test_case + 1))
    for i in range(N):
        for j in range(N):
            print(board[i][j], end=' ')
        print()

