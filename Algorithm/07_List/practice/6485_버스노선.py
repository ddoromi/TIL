import sys
sys.stdin = open('6485.txt')

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    bus_route = []
    stops = []

    for i in range(N):
        start, end = map(int, input().split())
        for j in range(start, end + 1):
            bus_route.append(j)

    P = int(input())

    for p in range(P):
        stops.append(int(input()))

    print('#{}'.format(test_case), end=' ')
    for i in range(P):
        count = 0
        for j in range(len(bus_route)):
            if stops[i] == bus_route[j]:
                count += 1
        print(count, end=' ')
    print()
