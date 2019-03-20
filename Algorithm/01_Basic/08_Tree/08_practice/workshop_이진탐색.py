import sys
sys.stdin = open('workshop.txt')

for test_case in range(10):
    N = int(input())
    tree = [0] * (N + 1)
    P = [0] * (N + 1)

    for i in range(N):
        data = list(input().split())
        index = int(data[0])

        if len(data) > 2:
            tree[index] = data[1]
            P[int(data[2])] = index
            P[int(data[3])] = index

        else:
            tree[index] = int(data[1])

    for j in range(N, 0, -2):
        if tree[P[j]] == '+':
            tree[P[j]] = tree[j-1] + tree[j]
        elif tree[P[j]] == '-':
            tree[P[j]] = tree[j-1] - tree[j]
        elif tree[P[j]] == '/':
            tree[P[j]] = tree[j-1] / tree[j]
        elif tree[P[j]] == '*':
            tree[P[j]] = tree[j-1] * tree[j]

    print('#{} {}'.format(test_case + 1, int(tree[1])))

