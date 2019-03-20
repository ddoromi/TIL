import sys
sys.stdin = open('5097.txt')


T = int(input())
for test_case in range(T):
    N, M = map(int, input().split())
    nums = list(map(int, input().split()))

    print('#{} {}'.format(test_case + 1, nums[M % N]))
