import sys
sys.stdin = open('1240.txt')

T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    data = []
    array = []
    result = confirm = 0
    for n in range(N):
        data.append((input()))
    code = {'0001101': 0, '0011001': 1, '0010011': 2, '0111101': 3,
            '0100011': 4, '0110001': 5, '0101111': 6,
            '0111011': 7, '0110111': 8, '0001011': 9}
    j = 0
    check = False
    while not check:
        i = M
        while i > 0:
            if data[j][i - 7:i] in code:
                array.insert(0, code[data[j][i - 7:i]])
                i -= 7
                check = True
            else:
                i -= 1
            if len(array) == 9:
                break
        j += 1
        if j == N:
            break

    array.insert(0, 0)
    for i in range(1, 9):
        if i % 2:
            confirm += 3 * array[i]
        else:
            confirm += array[i]
        result += array[i]
    if confirm % 10 != 0:
        result = 0
    print('#{} {}'.format(test_case, result))
