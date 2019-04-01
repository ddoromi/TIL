import sys
sys.stdin = open('1486.txt')

T = int(input())
for test_case in range(1, T + 1):
    N, B = map(int, input().split())
    H = list(map(int, input().split()))
    Min = B
    for i in range(1 << N):
        Sum = 0
        for j in range(N):
            if i & (1 << j):
                Sum += H[j]
        if Sum >= B:
            Min = min(Min, Sum - B)

    print('#{} {}'.format(test_case, Min))