import sys
sys.stdin = open('workshop.txt')


def check_right(data, start):
    if data[start[0]][start[1] + 1] == 1:
        data[start[0]][start[1]] = False
        start[1] = start[1] + 1
        return True
    else:
        return False


def check_left(data, start):
    if data[start[0]][start[1] - 1] == 1:
        data[start[0]][start[1]] = False
        start[1] = start[1] - 1
        return True
    else:
        return False


def column(data, start):
    data[start[0]] = False
    start[0] = start[0] - 1
    if start[0] == 0:
        print(f'#{test_case} {start[1]}')


for t in range(10):
    test_case = int(input())
    data = []

    for i in range(100):
        data.append(list(map(int, input().split())))

    for i in range(100):
        if data[99][i] == 2:
            start = [99, i]

    while start[0]:

        if start[1] == 0:  # 세로가 0일 때
            if check_right(data, start) == False:
                column(data, start)

        elif start[1] == 99:  # 세로가 9일 때
            if check_left(data, start) == False:
                column(data, start)

        else:
            if (check_right(data, start) == False) and (check_left(data, start) == False):
                column(data, start)
