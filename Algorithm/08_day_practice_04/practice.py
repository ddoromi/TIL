data = [9, 2, 10, 16, 10, 13, 16, 7, 11, 20, 20, 4, 13, 3, 11, 1, 10, 19, 2, 6, 18, 11, 10, 14, 13, 15, 5, 8, 13, 9, 9, 18, 16, 12, 20, 17, 9, 5,]
V, E = 20, 19
result = []
G = [[] for _ in range(V+1)]
visit = [False for _ in range(V+1)]

print(len(data))
for e in range(0, E*2, 2):
        G[data[e+1]].append(data[e])

print(G)

while E > 0:
    for i in range(1, V+1):
        if len(G[i]) == 0:
            result.append(i)
            G[i] = [0]
            print(i, end=' ')
            

    for i in result:
        if G[i] == 0:
            pass
        for j in range(1, V+1):
            if i in G[j]:
                G[j].remove(i)
                E -= 1


