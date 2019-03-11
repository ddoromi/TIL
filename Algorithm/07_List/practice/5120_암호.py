import sys
sys.stdin = open('5120.txt')



T = int(input())
for test_case in range(1, T+1):
    N, M, K = map(int, input().split())
    sequence = list(map(int, input().split()))
    index = M

    for i in range(K):
        index = index % len(sequence)
        value = sequence[index-1] + sequence[index]
        sequence.insert(index, value)
        index += M

    print('#{}'.format(test_case), end=' ')
    for i in range(1, 10):
        print(sequence[-i], end=' ')
    print()

