import sys
sys.stdin = open('1242.txt')
sys.stdout = open('out.txt', 'w')

T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    convert = {'A': [1, 0, 1, 0], 'B': [1, 0, 1, 1], 'C': [1, 1, 0, 0], 'D': [1, 1, 0, 1],
               'E': [1, 1, 1, 0], 'F': [1, 1, 1, 1]}
    data = []
    for i in range(N):
        data.append(list(input()))

    password = []
    for i in range(1, N):
        check = False
        for j in range(M):
            if not check and data[i][j] != '0' and data[i-1][j] == '0':
                li = []
                check = True
            elif check and data[i][j] != '0' and data[i-1][j] == data[i][j]:
                password.append(li)
                check = False
            if check:
                li.append(data[i][j])
        if check:
            password.append(li)
    for p in password:
        while p[-1] == '0':
            p.pop()

    print('#{} {}'.format(test_case, password))