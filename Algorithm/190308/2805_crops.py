import sys
sys.stdin = open('2805.txt')

T = int(input())
for test_case in range(T):
    N = int(input())
    farm = []
    Sum = index = 0

    for i in range(N):
        farm.append(list(input()))

    for i in range(N):
        Sum += int(farm[N//2][i])

    for i in range(N//2 - 1, -1, -1):
        index += 1
        for j in range(index, N - index):
            Sum += int(farm[i][j]) + int(farm[-i-1][j])

    print('#{} {}'.format(test_case + 1, Sum))
