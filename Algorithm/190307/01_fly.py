import sys
sys.stdin = open('01.txt')


def murder_fly(x, y, fly_sum):
    global Max

    if x == (N - M) + 1 or y == (N - M)+1:
        return

    for i in range(M):
        for j in range(M):
            fly_sum += data[y+i][x+j]

    if fly_sum > Max:
        Max = fly_sum

    murder_fly(x+1, y, 0)
    murder_fly(x, y+1, 0)


T = int(input())
for test_case in range(T):
    N, M = map(int, input().split())
    data = []
    Max = 0

    for i in range(N):
        data.append(list(map(int, input().split())))

    murder_fly(0, 0, 0)
    print('#{} {}'.format(test_case + 1, Max))