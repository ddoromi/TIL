import sys
sys.stdin = open('1861.txt')
from collections import deque

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    square = []
    room_number, Max = N ** 2, 0
    for i in range(N):
        square.append(list(map(int, input().split())))

    room = deque()
    for i in range(N):
        for j in range(N):
            room.append([i, j])
            count = 1
            while len(room):
                x, y = room.popleft()
                XY = [[x - 1, y], [x + 1, y], [x, y - 1], [x, y + 1]]
                for xy in XY:
                    if xy[0] in [-1, N] or xy[1] in [-1, N]:
                        continue
                    if square[xy[0]][xy[1]] - square[x][y] == 1:
                        room.append([xy[0], xy[1]])
                        count += 1
            if count == Max and square[i][j] < room_number:
                room_number = square[i][j]
            elif count > Max:
                room_number, Max = square[i][j], count
    print('#{} {} {}'.format(test_case, room_number, Max))


