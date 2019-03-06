import sys
sys.stdin = open('4835.txt')

T = int(input())
for test_case in range(T):
    N, M = map(int, input().split())
    nums = list(map(int, input().split()))
    Max, Min = 0, 30000

    for i in range(N - M + 1):
        Sum = 0
        for j in range(i, M):
            Sum += nums[j]
        Min = min(Min, Sum)
        Max = max(Max, Sum)

    print('#{} {}'.format(test_case + 1, Max - Min))

