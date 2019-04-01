import sys
sys.stdin = open('5209.txt')


def cost(n, Sum, index):
    global Min
    if Sum > Min:
        return
    if n == N:
        Min = min(Min, Sum)
        return
    for i in List:
        if not visit[i]:
            visit[i] = True
            cost(n + 1, Sum + MAP[index][i], index + 1)
            visit[i] = False

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    MAP = []
    for i in range(N):
        MAP.append(list(map(int, input().split())))
    List = [i for i in range(N)]
    Min = 0xffffff
    route = []
    visit = [False] * N
    cost(0, 0, 0)
    print('#{} {}'.format(test_case, Min))
