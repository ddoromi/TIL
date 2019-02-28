import sys
sys.stdin = open('4881.txt')

def perm(k, n, j):
    global Sum, Min
    if k == n:
        Sum = 0
        for i in range(n):
            Sum += order[i]
        if Min > Sum:
            Min = Sum
        return

    for i in range(n):
        if used[i]: continue

        used[i] = True
        order.append(nums[j][i])

        perm(k + 1, n, j + 1)
        used[i] = False
        order.pop()

T = int(input())
for test_case in range(T):
    N = int(input())
    nums = []

    for n in range(N):
        nums.append(list(map(int, input().split())))
    
    order = []
    Sum, Min = 0, 500
    used = [False] * len(nums)
    perm(0, N, 0)
    print(f'#{test_case+1} {Min}')