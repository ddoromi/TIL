import sys
sys.stdin = open('DFS_input.txt')
V, E = map(int, input().split())
G = [[] for _ in range(V+1)]

for i in range(E):
    u, v = map(int, input().split())
    G[u].append(v)
    G[v].append(u)

for i in range(1, V+1):
    print(i, G[i])


def DFS(start):
    visit = [False for _ in range(V+1)]
    S = []
    v = start
    visit[v] = True
    print(v, end=' ')
    S.append(v)

    while len(S) > 0:
        # v의 방문하ㅈ지 않은 인접 정접을 찾는다.
        goback = True
        for w in G[v]:
            if not visit[w]:
                visit[w] = True
                print(w, end=' ')
                S.append(v)
                v = w
                goback = False
                break
        if goback:
            v = S.pop(-1)


# 무향 그래프
