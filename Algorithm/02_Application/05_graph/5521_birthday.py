import sys
sys.stdin = open('5521.txt')

T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    friend = [[] for _ in range(N + 1)]
    for i in range(M):
        a, b = map(int, input().split())
        friend[a] += [b]
        friend[b] += [a]
    count = []
    count.extend(friend[1])
    for i in friend[1]:
        for j in friend[i]:
            if j not in count and j != 1:
                count += [j]
    print('#{} {}'.format(test_case, len(count)))

