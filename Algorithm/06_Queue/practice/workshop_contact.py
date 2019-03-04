import sys
from queue import Queue
sys.stdin = open('workshop.txt')


def BFS(s, G):
    D = [0] * 101
    visit = [False] * 101
    Max = 0
    Q = Queue()
    Q.put(s)
    visit[s] = True

    while not Q.empty():
        v = Q.get()
        for w in G[v]:
            if not visit[w]:
                D[w] = D[v] + 1
                visit[w] = True
                Q.put(w)

    for i in range(101):
        if Max <= D[i]:
            Max = D[i]
            idx = i

    return idx


for test_case in range(10):
    N, Start = map(int, input().split())
    data = list(map(int, input().split()))
    G = [[] for _ in range(101)]

    for i in range(0, N, 2):
        G[data[i]].append(data[i+1])

    print('#{} {}'.format(test_case + 1, BFS(Start, G)))



