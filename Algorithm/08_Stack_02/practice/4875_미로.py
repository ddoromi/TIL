import sys
sys.stdin = open('4875.txt')


def search(x, y):
    maze[x][y] = 1
    XY = [[x - 1, y], [x, y + 1], [x + 1, y], [x, y - 1]]
    for xy in XY:
        if maze[xy[0]][xy[1]] == 3:
            return 1
        elif maze[xy[0]][xy[1]] == 0:
           if search(xy[0], xy[1]): return 1
    return 0


T = int(input())
for test_case in range(T):
    N = int(input())
    maze = [[1 for i in range(N+2)]]

    for n in range(N):
        data = list(map(int, input()))
        maze.append([1] + data + [1])

    maze.append([1 for i in range(N+2)])

    for i in range(1, N+1):
        for j in range(1, N+1):
            if maze[i][j] == 2:
                start = [i, j]
                break

    stack = []
    print(f'#{test_case+1} {search(start[0],start[1])}')