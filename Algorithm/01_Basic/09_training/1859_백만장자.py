import sys
sys.stdin = open('1859.txt')

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    price = list(map(int, input().split()))
    start = profit = 0

    while start < N:
        Sum = count = Max = 0

        for i in range(start, N):
            if Max < price[i]:
                Max = price[i]
                index = i
        if Max:
            for i in range(start, index):
                Sum += price[i]
                count += 1
            profit += (Max * count) - Sum
            start = index + 1

        else:
            break

    print('#{} {}'.format(test_case, profit))