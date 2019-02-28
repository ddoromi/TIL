### 4831_그래프경로

```python
def DFS(v, t):
    visit[v] = True
    if v == t: return True
    for w in G[v]:
        if not visit[w]:
            if DFS(w, t): return True
	return False

T = int(input())
for t in range(T):
    V, E = map(int, input().split())
    G = [[] for _ in range(V+1)]
    visit = [False for _ in range(V+1)]

    for i in range(E):
        u, v = map(int, input().split())
        G[u].append(v)

    S, D = map(int, input().split())
    DFS(S, D)
    if visit[D]:
        print(f'#{t+1} 1')
    else:
        print(f'#{t+1} 0')
```

### 4869_종이붙이기

```python
def paper(n):
    if n == 1: return 1
    if n == 2: return 3
    if memo[n]: return memo[n]
    return paper(n - 1) + paper(n - 2)*2

memo = [0] * 31
T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    N /= 10
    
    ans = paper(N)
```

### workshop_그래프경로

```python
V, E = map(int, input().split())
G = [[] for _ in range(V + 1)]
arr = list(map(int, input().split()))
indeg = [0] * (V + 1)
visit = [False] * (V + 1)

for i in range(0, E * 2, 2):
    u, v = arr[i], arr[i + 1]
    G[u].append(v)
    indeg[v] += 1


while True:
    v = 0
    for i in range(1, V + 1):
        if not visit[i] and indeg[i] == 0:
            v = i
            break
    if v == 0: break
    print(v)  # 출력 또는 저장
    visit[v] = True
    
    for w in G[v]:
        if indeg[w]: indeg[w] -= 1
```





