import sys
sys.stdin = open('1491.txt')
import math
T = int(input())
for test_case in range(1, T + 1):
    N, A, B = map(int, input().split())
    Min = 0xfffffff
    R = int(math.sqrt(N))
    for i in range(R, 0, -1):
        C = N // i
        for j in range(C , 0, -1):
            xx = A * abs(i - j) + B * (N - i * j)
            if xx < 0:
                continue
            Min = min(Min, xx)
    print('#{} {}'.format(test_case, Min))
