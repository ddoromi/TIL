import sys
from itertools import combinations
sys.stdin = open('2.txt')

T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    data = []
    DP = [[0 for _ in range(M)] for _ in range(N)]
    for i in range(N):
        data.append(list(map(int, input().split())))
    DP[0][0] = data[0][0]
    column = list(combinations([i for i in range(M - 1)], 2))
    row = []
    for i in range(len(column)):
        column[i] = list(column[i]) + [M - 1]
    for i in range(N - 1):
        row.append([i, N - 1])

    # DP의 첫 번째 행
    for j in range(1, M):
        DP[0][j] = DP[0][j - 1] + data[0][j]
    # DP의 첫 번째 열
    for j in range(1, N):
        DP[j][0] = DP[j - 1][0] + data[j][0]
    # DP의 나머지
    for i in range(1, N):
        for j in range(1, M):
            DP[i][j] = data[i][j] + DP[i - 1][j] + DP[i][j - 1] - DP[i - 1][j - 1]

    sum_index = list(combinations([i for i in range(6)], 3))
    for i in range(len(sum_index)):
        sum_index[i] = list(sum_index[i]) + [sum_index[i][0]]
    Max = 0
    for rr in row:
        for cc in column:
            index = []
            for i in rr:
                for j in cc:
                    index.append([i, j])

            sums = []
            for xy in range(6):
                if xy == 0:
                    sums.append(DP[index[0][0]][index[0][1]])
                elif 1 <= xy < 3:
                    sums.append(DP[index[xy][0]][index[xy][1]] - DP[index[xy - 1][0]][index[xy - 1][1]])
                elif xy == 3:
                    sums.append(DP[index[xy][0]][index[xy][1]] - DP[index[xy - 3][0]][index[xy - 3][1]])
                else:
                    sums.append(DP[index[xy][0]][index[xy][1]] - DP[index[xy - 3][0]][index[xy - 3][1]]
                                - DP[index[xy - 1][0]][index[xy - 1][1]]  + DP[index[xy - 4][0]][index[xy - 4][1]])
            for ss in sum_index:
                Sum = 0
                for k in range(1, len(ss)):
                    Sum += abs(sums[ss[k]] - sums[ss[k - 1]])
                Max = max(Max, Sum)
    print('#{} {}'.format(test_case, Max))





