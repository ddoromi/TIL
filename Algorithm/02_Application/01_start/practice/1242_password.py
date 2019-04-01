import sys
sys.stdin = open('1242.txt')

T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    convert = {'A': [1, 0, 1, 0], 'B': [1, 0, 1, 1], 'C': [1, 1, 0, 0], 'D': [1, 1, 0, 1],
               'E': [1, 1, 1, 0], 'F': [1, 1, 1, 1]}
    data = []
    PASSWORD = []

    # 암호코드가 포함된 행 찾기
    for i in range(N):
        data.append(list(input()))

    for i in range(N):
        for j in range(M):
            if data[i][j] != '0' and data[i] not in PASSWORD:
                PASSWORD.append(data[i])
                break

    # 암호코드 이진법으로 변환하기
    binary = []
    for password in PASSWORD:
        trash = True
        check_i = []
        for j in password:
            check = []
            if j == '0' and trash:
                check += [0]
            elif j == '0' and not trash:
                check += [0] * 4
                trash = True
            else:
                trash = False
                if j in convert:
                    check += convert[j]
                else:
                    j = int(j)
                    count, n = 0, []
                    while count < 4:
                        if j == 0:
                            remainder = 0
                        else:
                            remainder = j % 2
                            j //= 2
                        n.insert(0, remainder)
                        count += 1
                    check += n
            check_i += check
        binary.append(check_i)

    password = {'3211': [0], '2221': [1], '2122': [2], '1411': [3],
                '1132': [4], '1231': [5], '1114': [6], '1312': [7],
                '1213': [8], '3112': [9]}

    converted = []
    for string in binary:
        count = n = 1
        array = []
        trash = True
        for i in range(len(string) - 1, -1, -1):
            if string[i] == 1:
                trash = False
            if not trash:
                if n % 7 == 0:
                    count = 0
                if string[i] != string[i - 1]:
                    count = 1
                    array.insert(0, count)
                elif string[i] == string[i - 1]:
                    count += 1
                n += 1
            i -= 1
        converted.append(array)


    print('#{} {}'.format(test_case, converted))