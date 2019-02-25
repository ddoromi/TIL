G = [[], [4], [1], [2], [], [1, 8], [5, 7], [2], [], [8]]
visit = [False, False, False, False, False, False, False, False, False, False]
V = E = 9
result = []

while E > 0:
    for i in range(1, V+1):
        if len(G[i]) == 0:
            result.append(i)
            G[i] = [False]
            print(i, end=' ')

    for i in result:
        for j in range(1, V+1):
            if i in G[j]:
                G[j].remove(i)
                E -= 1


