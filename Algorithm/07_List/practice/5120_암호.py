import sys
sys.stdin = open('5120.txt')


T = int(input())
for test_case in range(1, T+1):
    N, M, K = map(int, input().split())
    sequence = list(map(int, input().split()))
    index, count = 0, 1

    while count <= K:
        index = (index + M) % len(sequence)
        val = sequence[index - 1] + sequence[index]
        if index:
            sequence.insert(index, val)
        else:
            sequence.append(val)
            index = -1
        count += 1

    print('#{}'.format(test_case), end=' ')
    if len(sequence) > 10:
        for i in range(1, 11):
            print(sequence[-i], end=' ')
    else:
        for i in range(1, len(sequence)+1):
            print(sequence[-i], end =' ')
    print()


