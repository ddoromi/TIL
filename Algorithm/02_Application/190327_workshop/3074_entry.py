import sys
sys.stdin = open('3074.txt')

T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    K = []
    for i in range(N):
        K.append(int(input()))
    K.sort()
    memo = [0] * N
    memo[0] = M

    for k in range(N):
        for i in range(N):
            for j in range(i + 1, N):
                if K[i] * (memo[i]) > K[j] * (memo[j] + 1):
                    memo[i] -= 1
                    memo[i + 1] += 1

    Max = max(memo[i] * K[i] for i in range(N))
    print(memo)
    print('#{} {}'.format(test_case, Max))

