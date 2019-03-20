import sys
sys.stdin = open('3750.txt')

result = []
T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    while N // 10:
        Sum = 0
        while N:
            Sum += N % 10
            N //= 10
        N = Sum
    result += [N]

for i in range(1, T + 1):
    print('#{} {}'.format(i, result[i-1]))