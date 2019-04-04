import sys
from itertools import permutations
sys.stdin = open('5189.txt')

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    MAP = []
    for i in range(N):
        MAP.append(list(map(int, input().split())))
    office = [i for i in range(1, N)]
    route = list(permutations(office, N - 1))
    Min = 0xffff
    for nums in route:
        Sum = MAP[0][nums[0]]
        for j in range(len(nums) - 1):
            Sum += MAP[nums[j]][nums[j + 1]]
            if Sum >= Min:
                break
        else:
            Sum += MAP[nums[j + 1]][0]
            Min = min(Min, Sum)
    print('#{} {}'.format(test_case, Min))