import sys
sys.stdin = open('5177.txt')

T = int(input())
for test_case in range(T):
    N = int(input())
    nodes = [0] + list(map(int, input().split()))
    tree = [0, nodes[1]]
    j, p_sum, p = 2, 0, N//2

    for i in range(2, N + 1):
        tree.append(nodes[i])
        index = i // 2
        j = i
        while index >= 1:
            if tree[index] > tree[j]:
                tree[index], tree[j] = tree[j], tree[index]
            j = index
            index //= 2

    while p >= 1:
        p_sum += tree[p]
        p //= 2

    print('#{} {}'.format(test_case + 1, p_sum))








