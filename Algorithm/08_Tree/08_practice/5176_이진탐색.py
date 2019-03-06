import sys
sys.stdin = open('5176.txt')


def binary_tree(node):
    global traversal
    if node == 0:
        return

    binary_tree(L[node])
    traversal.append(node)
    binary_tree(R[node])


T = int(input())
for test_case in range(T):
    N = int(input())
    L = [0] * (N + 1)
    R = [0] * (N + 1)
    traversal = [0]
    j, k, S = 1, 0, 0

    for i in range(2, N + 1, 2):
        L[j] = i
        if N % 2 == 0 and i == N:
            break
        R[j] = i + 1
        j += 1

    binary_tree(1)
    print('#{} {} {}'.format(test_case + 1, traversal.index(1), traversal.index(N//2)))

