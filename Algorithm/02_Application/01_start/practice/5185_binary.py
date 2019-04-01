import sys
sys.stdin = open('5185.txt')

T = int(input())
for test_case in range(1, T + 1):
    N, num = input().split()
    N, num = int(N), list(num)
    convert = {'A': '1010', 'B': '1011', 'C': '1100', 'D': '1101', 'E': '1110', 'F': '1111'}
    result = []
    for i in range(int(N)):
        if num[i] in convert:
            result += list(convert[num[i]])
        else:
            num[i] = int(num[i])
            n = []
            count = 0
            while count < 4:
                if num[i] == 0:
                    remainder = 0
                else:
                    remainder = num[i] % 2
                    num[i] //= 2
                n.insert(0, remainder)
                count += 1
            result += n
    print('#{}'.format(test_case), end=' ')
    for j in result:
        print(j, end='')
    print()

