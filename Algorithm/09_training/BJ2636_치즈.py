import sys, copy
sys.stdin = open('BJ2636.txt')


def hole(x, y):
    global stack_0
    XY = [[x - 1, y], [x + 1, y], [x, y - 1], [x, y + 1]]
    if (x <= 2 or y <= 2) or (x >= N - 2 or y >= M - 2):
        stack_0 = []
        return

    stack_0.append([x, y])
    cheese_copy[x][y] = 3

    for dxy in XY:
        if cheese_copy[dxy[0]][dxy[1]] == 0:
            if [dxy[0], dxy[1]] not in stack_0:
                hole(dxy[0], dxy[1])
        else:
            continue
    return


def search(x, y):
    XY = [[x - 1, y], [x + 1, y], [x, y - 1], [x, y + 1]]
    for xy in XY:
        if cheese[xy[0]][xy[1]] == 0 and ([xy[0], xy[1]] not in stack_hole):
            return 1


N, M = map(int, input().split())
cheese = []
count = 0

for i in range(N):
    cheese.append(list(map(int, input().split())))

while True:
    cheese_copy = copy.deepcopy(cheese)
    stack_hole = []
    stack_1 = []
    for i in range(2, N - 2):
        for j in range(2, M - 2):
            if cheese_copy[i][j] == 0 and (cheese_copy[i][j - 1] == 1 and cheese_copy[i - 1][j] == 1):
                stack_0 = []
                hole(i, j)
                if stack_0:
                    stack_hole += stack_0

    for i in range(1, N - 1):
        for j in range(1, M - 1):
            if cheese[i][j] == 1 and search(i, j):
                stack_1.append([i, j])

    if len(stack_1) > 0 and len(stack_hole) == 0:
        count_1 = len(stack_1)

    if len(stack_1) == 0:
        break

    count += 1
    for xy in stack_1:
        cheese[xy[0]][xy[1]] = 0

print(count)
print(count_1)