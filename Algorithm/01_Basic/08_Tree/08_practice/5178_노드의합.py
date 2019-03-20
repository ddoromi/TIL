import sys
sys.stdin = open('5178.txt')

T = int(input())
for test_case in range(T):
    N, M, L = map(int, input().split())
    nums = [0] * (N + 1)
    C, P = N, N // 2

    for i in range(M):
        node, num = map(int, input().split())
        nums[node] = num

    while P >= 1:
        nums[P] += nums[C]
        C -= 1
        P = C // 2

    print('#{} {}'.format(test_case + 1, nums[L]))
