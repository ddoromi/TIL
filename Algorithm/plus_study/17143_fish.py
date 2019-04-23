import sys
sys.stdin = open('17143.txt')


def direction(shark, x, y, s, dir):
    if s == 0:
        shark[0], shark[1] = x, y
        return
    XY = [0, [x - 1, y], [x + 1, y], [x, y + 1], [x, y - 1]]
    if dir == 1 and x == 0:
        direction(shark, x, y, s, 2)
    elif dir == 2 and x == R - 1:
        direction(shark, x, y, s, 1)
    elif dir == 3 and y == C - 1:
        direction(shark, x, y, s, 4)
    elif dir == 4 and y == 0:
        direction(shark, x, y, s, 3)
    else:
        direction(shark, XY[dir][0], XY[dir][1], s - 1, dir)


for test_case in range(4):
    R, C, M = map(int, input().split())
    sharks_index = []
    sharks = []
    visited = [False for _ in range(M)]
    result = 0

    for i in range(M):
        r, c, s, d, z = map(int, input().split())
        sharks.append([r - 1, c - 1, s, d, z])

    for i in range(C):
        MAP = [[0 for _ in range(C)] for _ in range(R)]
        for shark in sharks:
            if shark:
                direction(shark, shark[0], shark[1], shark[2], shark[3])

        for s in range(M):
            if sharks[s]:
                if MAP[sharks[s][0]][sharks[s][1]] != 0:
                    if MAP[sharks[s][0]][sharks[s][1]][4] < sharks[s][4]:
                        MAP[sharks[s][0]][sharks[s][1]] = sharks[s] + [s]
                        sharks[MAP[sharks[s][0]][sharks[s][1]][5]] = False
                    else:
                        sharks[s] = False
                else:
                    MAP[sharks[s][0]][sharks[s][1]] = sharks[s] + [s]

        for j in range(R):
            if MAP[j][i] != 0:
                result += MAP[j][i][4]
                sharks[MAP[j][i][5]] = False
                break

    print(result)