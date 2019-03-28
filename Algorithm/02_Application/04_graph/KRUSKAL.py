p = [i for i in range(10)]

def find_set(x):
    if x != p[x]:
        p[x] = find_set(p[x])
    return p[x]

def union(x, y):
    p[y] = x

V, E = map(int, input().split())
edges, tree = [], []

for i in range(E):
    u, v, w = map(int, input().split())
    edges.append((u, v, w))

edges.sort(key=lambda x: x[2])
cnt = V - 1
while cnt > 0:
    u, v, w = edges.pop(0)
    a = find_set(u)
    b = find_set(v)
    if a == b:
        continue
    tree.append((u, v, w))
    union(a, b)
    cnt -= 1