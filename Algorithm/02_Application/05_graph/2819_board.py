import sys
sys.stdin = open('2819.txt')


def board(n, x, y):
    global num
    num += data[x][y]
    if n == 6:
        if num not in nums:
            nums.append(num)
        return
    XY = [[x - 1, y], [x + 1, y], [x, y - 1], [x, y + 1]]
    for xy in XY:
        if 0 <= xy[0] < 4 and 0 <= xy[1] < 4:
            board(n + 1, xy[0], xy[1])
            num = num[:-1]

T = int(input())
for test_case in range(1, T + 1):
    data = []
    nums = []
    for i in range(4):
        data.append(input().split())

    for i in range(4):
        for j in range(4):
            num = ''
            board(0, i, j)
    print('#{} {}'.format(test_case, len(nums)))
