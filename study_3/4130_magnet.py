import sys
sys.stdin = open('4130.txt')

T = int(input())
for test_case in range(1, T + 1):
    K = int(input())
    magnet = []
    Sum = 0
    for i in range(4):
        magnet.append(list(map(int, input().split())))

    for i in range(K):
        index, direction = map(int, input().split())
        check = [False for _ in range(4)]
        if index - 1 == 0:
            if direction == 1:
                check[0] = 1
                if magnet[0][0] != magnet[1][0]:
                    check[1] = -1
                    if magnet[1][0] != magnet[2][0]:
                        check[2] = 1
                        if magnet[2][0] != magnet[3][0]:
                            check[3] = -1
            elif direction == -1:
                check[0] = -1
                if magnet[0][0] != magnet[1][0]:
                    check[1] = 1
                    if magnet[1][0] != magnet[2][0]:
                        check[2] = -1
                        if magnet[2][0] != magnet[3][0]:
                            check[3] = 1
        if index - 1 == 1:
            if direction == 1:
                check[1] = 1
                if magnet[1][0] != magnet[0][0]:
                    check[0] = -1
                if magnet[1][0] != magnet[2][0]:
                    check[2] = -1
                    if magnet[2][0] != magnet[3][0]:
                        check[3] = 1
            elif direction == -1:
                check[1] = -1
                if magnet[1][0] != magnet[0][0]:
                    check[0] = 1
                if magnet[1][0] != magnet[2][0]:
                    check[2] = 1
                    if magnet[2][0] != magnet[3][0]:
                        check[3] = -1
        if index - 1 == 2:
            if direction == 1:
                check[2] = 1
                if magnet[2][0] != magnet[1][0]:
                    check[1] = -1
                    if magnet[1][0] != magnet[0][0]:
                        check[0] = 1
                if magnet[2][0] != magnet[3][0]:
                    check[3] = -1
            elif direction == -1:
                check[2] = -1
                if magnet[2][0] != magnet[1][0]:
                    check[1] = 1
                    if magnet[1][0] != magnet[0][0]:
                        check[0] = -1
                if magnet[2][0] != magnet[3][0]:
                    check[3] = 1
        if index - 1 == 3:
            if direction == 1:
                check[3] = 1
                if magnet[3][0] != magnet[2][0]:
                    check[2] = -1
                    if magnet[2][0] != magnet[1][0]:
                        check[1] = 1
                        if magnet[1][0] != magnet[0][0]:
                            check[0] = -1
            elif direction == -1:
                check[3] = -1
                if magnet[3][0] != magnet[2][0]:
                    check[2] = 1
                    if magnet[2][0] != magnet[1][0]:
                        check[1] = -1
                        if magnet[1][0] != magnet[0][0]:
                            check[0] = 1

        for j in range(4):
            if check == 1:
                magnet[j][0], magnet[j][1], magnet[j][2], magnet[j][3], magnet[j][4], magnet[j][5], magnet[j][6], magnet[j][7] \
                        = magnet[j][7], magnet[j][0], magnet[j][1], magnet[j][2], magnet[j][3], magnet[j][4], magnet[j][5], magnet[j][6]
            elif check == -1:
                magnet[j][0], magnet[j][1], magnet[j][2], magnet[j][3], magnet[j][4], magnet[j][5], magnet[j][6], magnet[j][7] \
                    = magnet[j][1], magnet[j][2], magnet[j][3], magnet[j][4], magnet[j][5], magnet[j][6], magnet[j][7], magnet[j][0]

    if magnet[0][0] == 1:
        Sum += 1
    if magnet[0][2] == 1:
        Sum += 2
    if magnet[0][3] == 1:
        Sum += 4
    if magnet[0][4] == 1:
        Sum += 8

    print('#{} {}'.format(test_case, Sum))