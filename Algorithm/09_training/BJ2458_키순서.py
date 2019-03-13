import sys
sys.stdin = open('BJ2458.txt')


def search(v, D):
    global s_count, t_count
    visit[v] = True
    if D == 'S':
        for w in shorter[v]:
            if not visit[w]:
                s_count += 1
                search(w, 'S')

    else:
        for w in taller[v]:
            if not visit[w]:
                t_count += 1
                search(w, 'T')


N, M = map(int, input().split())
taller = [[] for _ in range(N + 1)]
shorter = [[] for _ in range(N + 1)]
count = 0

for i in range(M):
    u, v = map(int, input().split())
    taller[u].append(v)
    shorter[v].append(u)

for i in range(1, N + 1):
    visit = [False for _ in range(N + 1)]
    s_count = t_count = 0

    if shorter[i]:
        for short in shorter[i]:
            if visit[short]:
                continue
            s_count += 1
            search(short, 'S')

    if taller[i]:
        for tall in taller[i]:
            if visit[tall]:
                continue
            t_count += 1
            search(tall, 'T')

    if s_count + t_count == N - 1:
        count +=1

print(count)


