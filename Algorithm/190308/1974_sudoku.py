import sys
sys.stdin = open('1974.txt')

T = int(input())
for test_case in range(T):
    board = []
    result = 1

    for i in range(9):
        board.append(list(map(int, input().split())))

    for i in range(9):
        stack_row = []
        stack_column = []
        for j in range(9):
            if board[i][j] in stack_row:
                result = 0
                break
            else:
                stack_row.append(board[i][j])
            if board[j][i] in stack_column:
                result = 0
                break
            else:
                stack_column.append(board[j][i])

    if result:
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                stack_rectangle = []
                for k in range(3):
                    for l in range(3):
                        if board[i+k][j+l] in stack_rectangle:
                            result = 0
                            break
                        else:
                            stack_rectangle.append(board[i][j])

    print('#{} {}'.format(test_case + 1, result))
