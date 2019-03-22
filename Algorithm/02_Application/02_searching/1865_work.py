import sys
sys.stdin = open('1865.txt')


def work(k ,n ,j, probability):
    global Max
    if k == n:
        if Max < probability:
            Max = probability
        return
    if probability < Max:
        return
    for i in range(n):
        if used[i]: continue
        used[i] = True
        work(k + 1, n, j + 1, probability * 0.01 * data[j][i])
        used[i] = False

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    data = []
    for i in range(N):
        data.append(list(map(int, input().split())))

    Max = 0
    used = [False] * N
    work(0, N, 0, 1)
    print('#{} {}'.format(test_case, format(Max * 100, '2.6f')))