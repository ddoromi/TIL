import sys
sys.stdin = open('5189.txt')


def electric_cart(n , k):
    if k == n:
        print(office)
        return
    else:
        for i in range(k, n):
            office[k], office[i] = office[i], office[k]
            electric_cart(n, k + 1)
            office[k], office[i] = office[i], office[k]

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    MAP = []
    for i in range(N):
        MAP.append(list(map(int, input().split())))
    office = [i for i in range(1, N + 1)]

    electric_cart(N, 0)