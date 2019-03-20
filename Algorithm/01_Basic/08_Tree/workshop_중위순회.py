import sys
sys.stdin = open('workshop.txt')


def inorder(v):
    global result
    if v == 0:
        return

    inorder(L[v])
    result += array[v]
    inorder(R[v])


for test_case in range(10):
    N = int(input())
    L = [0] * (N + 1)
    R = [0] * (N + 1)
    P = [0] * (N + 1)
    array = [[] for _ in range(N + 1)]
    result = ''

    for i in range(N):
        data = list(input().split())
        array[int(data[0])] = data[1]

        if len(data) == 4:
            L[int(data[0])] = int(data[2])
            R[int(data[0])] = int(data[3])
            P[int(data[2])] = int(data[0])
            P[int(data[3])] = int(data[0])

        if len(data) == 3:
            L[int(data[0])] = int(data[2])
            R[int(data[0])] = 0
            P[int(data[2])] = int(data[0])
    print(array)
    inorder(1)
    print('#{} {}'.format(test_case + 1, result))

