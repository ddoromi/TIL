import sys
sys.stdin = open('BJ1890.txt')
sys.setrecursionlimit(0xfffffff)


def jump(x, y, num):
    global count
    XY = [[x + num, y], [x, y + num]]
    for xy in XY:
        if xy[0] > N - 1 or xy[1] > N - 1:
            continue
        if board[xy[0]][xy[1]] > 0:
            jump(xy[0], xy[1], board[xy[0]][xy[1]])
        else:
            count += 1
            return

N = int(input())
board = []
count = 0
for i in range(N):
    board.append(list(map(int, input().split())))
jump(0, 0, board[0][0])
print(count)