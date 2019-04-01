import sys
from itertools import permutations
sys.stdin = open('3.txt')

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    snack = []
    robot = []

    array = list(map(int, input().split()))
    for i in range(0, N * 2, 2):
        snack.append([array[i], array[i + 1]])

    array = list(map(int, input().split()))
    for i in range(0, N * 2, 2):
        robot.append([array[i], array[i + 1]])

    comb = list(permutations([i for i in range(N)], N))
    for cc in range(len(comb)):
        comb[cc] = list(comb[cc])

    Min = 0xffffffff
    for cc in comb:
        Sum = 0
        for i in range(len(cc)):
            sx, sy = snack[i][0], snack[i][1]
            rx, ry = robot[cc[i]][0], robot[cc[i]][1]
            Sum += abs(sx - rx) + abs(sy - ry)
        Min = min(Min, Sum)
    print('#{} {}'.format(test_case, Min))




