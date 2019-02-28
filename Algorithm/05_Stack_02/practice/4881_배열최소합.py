import sys
sys.stdin = open('4881.txt')

T = int(input())
for test_case in range(T):
    N = int(input())
    nums = []
    Sum = 0
    visit = []
    arr = []
    Sum = 0
    order = [0] * N

    for n in range(N):
        nums.append(list(map(int, input().split())))

    prnit(min_sum(N,0))



def min_sum(N, j):
    global Sum
    if j == N:
        return
    visit = [False] * N

    for i in range(N):
        if visit[i]:
            continue
        order[j] = nums[j][i]
        visit[i] = True
        min_sum(N, j+1)