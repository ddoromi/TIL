import sys
from queue import Queue
sys.stdin = open('5102.txt')

def BFS(s, G):

    visit = [False] * (V + 1)
    D = [0] * (V + 1)

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
    print(D)
    return D[End]


T = int(input())
for test_case in range(T):
    V, E = map(int, input().split())
    G = [[] for _ in range(V + 1)]
    count = 0

    for i in range(E):
        u, v = map(int, input().split())
        G[u].append(v)
        G[v].append(u)

    Start, End = map(int, input().split())
    print('#{} {}'.format(test_case + 1, BFS(Start, G)))

