N, M = map(int, input().split())
nums = list(map(int, input().split()))
n, Max = 3, 0
order = [0]*n


def three(k, n, N, visit):
    global Max
    if k == n:
        Sum = 0
        for number in order:
            Sum += nums[number]
        if M >= Sum > Max:
            Max = Sum
        return Max

    for i in range(N):
        if visit & (1 << i):
            continue
        order[k] = i
        if k > 0 and order[k] < order[k-1]:
            continue
        three(k+1, 3, N, visit | (1 << i))


three(0, n, N, 0)
print(Max)
