import sys
sys.stdin = open('5122.txt')

T = int(input())
for test_case in range(1, T+1):
    N, M, L = map(int, input().split())
    sequence = list(map(int, input().split()))
    plus = []

    for i in range(M):
        plus.append(input().split())

    for i in range(M):
        if plus[i][0] == 'I':
            sequence.insert(int(plus[i][1]), int(plus[i][2]))
        elif plus[i][0] == 'D':
            sequence.remove(sequence[int(plus[i][1])])
        else:
            sequence[int(plus[i][1])] = int(plus[i][2])

    if len(sequence) <= L:
        result = -1
    else:
        result = sequence[L]
    print('#{} {}'.format(test_case, result))
