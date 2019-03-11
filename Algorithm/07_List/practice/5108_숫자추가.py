import sys
sys.stdin = open('5108.txt')

T = int(input())
for test_case in range(1, T + 1):
    N, M, L = map(int, input().split())
    sequence = list(map(int, input().split()))

    for i in range(M):
        index, num = map(int, input().split())
        sequence.insert(index, num)

    print('#{} {}'.format(test_case, sequence[L]))




