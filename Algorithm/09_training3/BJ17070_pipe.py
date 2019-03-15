import sys
sys.stdin = open('BJ17070.txt')


def search(x, y, direction):
    global count
    if x == N and y == N:
        count += 1
        return
    if direction == 'right':
        if floor[x][y + 1] == 0:
            search(x, y + 1, 'right')
            if (floor[x + 1][y] == 0) and (floor[x + 1][y + 1] == 0):
                search(x + 1, y + 1, 'cross')
    elif direction == 'down':
        if floor[x + 1][y] == 0:
            search(x + 1, y, 'down')
            if floor[x][y + 1] == 0 and floor[x + 1][y + 1] == 0:
                search(x + 1, y + 1, 'cross')
    else:
        if floor[x][y + 1] == 0:
            search(x, y + 1, 'right')
        if floor[x + 1][y] == 0:
            search(x + 1, y, 'down')
        if floor[x][y + 1] == 0 and floor[x + 1][y] == 0 and floor[x + 1][y + 1] == 0:
            search(x + 1, y + 1, 'cross')

for test_case in range(4):
    count = 0
    N = int(input())
    floor = [[1 for _ in range(N + 2)]]
    for i in range(N):
        floor.append([1] + list(map(int, input().split())) + [1])
    floor.append([1 for _ in range(N + 2)])
    search(1, 2, 'right')

    print(count)

