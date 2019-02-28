import sys
sys.stdin = open('workshop.txt')

for t in range(10):
    V, E = map(int, input().split())
    data = list(map(int, input().split()))
    G = [[] for _ in range(V+1)]

    for e in range(0, E*2, 2):
        G[data[e+1]].append(data[e])

    print(f'#{t+1}', end=' ')
    while E > 0:
        result = []
        for i in range(1, V+1):
            if len(G[i]) == 0:
                result.append(i)
                G[i] = [0]
                print(i, end=' ')

        for i in result:
            for j in range(1, V+1):
                if i in G[j]:
                    G[j].remove(i)
                    E -= 1
                    if E == 0:
                        print(j)
