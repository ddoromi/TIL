import sys
sys.stdin = open('1946.txt')

T= int(input())
for test_case in range(1, T + 1):
    N = int(input())
    string = []

    for i in range(N):
        char, num = input().split()
        num = int(num)
        string.append([char, num])

    print('#{}'.format(test_case))
    count = 0
    for i in range(N):
        for j in range(string[i][1]):
            if count == 10:
                print()
                count = 0
            print(string[i][0], end='')
            count += 1
    print()

