import sys
sys.stdin = open('4871.txt')


def DFS(v):
    visit[v] = True
    print(v, end=' ')
    for w in G[v]:
        if not visit[w]:
            DFS(w)


T = int(input())
for t in range(T):
    V, E = map(int, input().split())
    G = [[] for _ in range(V+1)]
    visit = [False for _ in range(V+1)]

    for i in range(E):
        u, v = map(int, input().split())
        G[u].append(v)

    S, D = map(int, input().split())
    DFS(S)
    if visit[D]:
        print(f'#{t+1} 1')
    else:
        print(f'#{t+1} 0')
