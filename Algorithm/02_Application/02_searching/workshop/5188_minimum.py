import sys
sys.stdin = open('5188.txt')

def minimum_sum(x, y, Sum):
    global Min
    XY = [[x + 1, y], [x, y + 1]]
    Sum += data[x][y]
    if x == N - 1 and y == N - 1:
        if Sum < Min:
            Min = Sum
    for xy in XY:
        if xy[0] > N - 1 or xy[1] > N - 1:
            continue
        if Sum > Min:
            break
        minimum_sum(xy[0], xy[1], Sum)

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    data = []
    Min = 0xffff

    for n in range(N):
        data.append(list(map(int, input().split())))
    minimum_sum(0, 0, 0)
    print('#{} {}'.format(test_case, Min))