import sys
sys.stdin = open('BJ2606.txt')

def DFS(v):
    visit[v] = True

    for w in graph[v]:
        if not visit[w]:
            DFS(w)

computer = int(input())
connect = int(input())
graph = [[] for _ in range(computer + 1)]
visit = [False for _ in range(computer + 1)]
count = 0

for i in range(connect):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

DFS(1)

for i in range(2, computer + 1):
    if visit[i] == True:
        count +=1

print(count)