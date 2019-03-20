import sys
sys.stdin = open('6057.txt')

T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    graph = [[] for i in range(N + 1)]
    triangle = 0

    for i in range(M):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)
        for j in graph:
            if u in j and v in j:
                triangle += 1




    print('#{} {}'.format(test_case, triangle))