import sys
sys.stdin = open('03.txt')

T = int(input())
for test_case in range(T):
    N, K = map(int, input().split())
    puzzle = []
    result = 0

    for i in range(N):
        puzzle.append(list(map(int, input().split())))

    for i in range(N):
        len_1 = 0
        for j in range(N):
            if puzzle[i][j] == 1:
                len_1 += 1
            else:
                if len_1 == K:
                    result += 1
                len_1 = 0
        if len_1 == K:
            result += 1

    for j in range(N):
        len_1 = 0
        for i in range(N):
            if puzzle[i][j] == 1:
                len_1 += 1
            else:
                if len_1 == K:
                    result += 1
                len_1 = 0
        if len_1 == K:
            result += 1

    print('#{} {}'.format(test_case + 1, result))