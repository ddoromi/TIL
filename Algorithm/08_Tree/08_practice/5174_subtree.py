import sys
sys.stdin = open('5174.txt')


def subtree(node):
    global count
    if node == 0:
        return

    count += 1
    subtree(L[node])
    subtree(R[node])


T = int(input())
for test_case in range(T):
    E, N = map(int, input().split())
    data = list(map(int, input().split()))
    L = [0] * (E + 2)
    R = [0] * (E + 2)
    count = 0

    for i in range(0, E*2, 2):
        if L[data[i]] == 0:
            L[data[i]] = data[i + 1]
        else:
            R[data[i]] = data[i + 1]

    subtree(N)
    print('#{} {}'.format(test_case + 1, count))
