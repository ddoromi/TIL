import sys
sys.stdin = open('4613.txt')

T = int(input())
for teat_case in range(1, T + 1):
    N, M = map(int, input().split())
    data = []
    Min = 2500

    for i in range(N):
        data.append(list(input()))

    Sum = 0
    for i in range(N):
        for j in range(M):
            if i == 0 and data[i][j] != 'W':
                Sum += 1
            elif i == N - 1 and data[i][j] != 'R':
                Sum += 1

    for i in range(N - 1):
        for j in range(N - 1 - i):
            if j == 0: continue
            total = Sum
            for w in range(1, i + 1):
                for l in range(M):
                    if data[w][l] != 'W':
                        total += 1
            for b in range(i + 1, i + 1 + j):
                for l in range(M):
                    if data[b][l] != 'B':
                        total += 1
            for r in range(i + j + 1, N - 1):
                for l in range(M):
                    if data[r][l] != 'R':
                        total += 1
            if Min > total:
                Min = total

    print('#{} {}'.format(teat_case, Min))
