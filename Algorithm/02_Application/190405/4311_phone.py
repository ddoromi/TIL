import sys
sys.stdin = open('4311.txt')


def smart_phone(k, sum):
    if k == N - 1:
        return
    for i in range(N):
        if operator[]
T = int(input())
for test_case in range(1, T + 1):
    N, O, M = map(int, input().split())
    nums = list(map(int, input().split()))
    data = list(map(int, input().split()))
    want = input()
    operator = [0, 0, 0, 0]
    result, Min, check_cnt = -1, M, 0

    for i in range(O):
        operator[data[i] - 1] = 1
    for i in range(len(want)):
        for n in nums:
            if int(want[i]) == n:
                check_cnt += 1
    if check_cnt == len(want):
        result = check_cnt
    else:


