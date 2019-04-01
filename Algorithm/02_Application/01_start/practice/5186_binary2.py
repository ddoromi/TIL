import sys
sys.stdin = open('5186.txt')

T = int(input())
for test_case in range(1, T + 1):
    N = float(input())
    result = []
    while N != 0:
        N *= 2
        if N >= 1:
            result.append(1)
            N -= 1
        else:
            result.append(0)
    print('#{}'.format(test_case), end=' ')
    if len(result) > 12:
        print('overflow')
    else:
        for i in result:
            print(i, end='')
        print()
