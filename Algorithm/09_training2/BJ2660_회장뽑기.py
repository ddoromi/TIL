import sys
sys.stdin = open('BJ2660.txt')


N = int(input())
friend = [[] for _ in range(N + 1)]
Min = 51
while True:
    p1, p2 = map(int, input().split())
    if p1 == -1:
        break
    friend[p1].append(p2)
    friend[p2].append(p1)

for i in range(1, N + 1):
    course = [i]
    distance = [0]
    visit = [False for _ in range(N + 1)]
    visit[i] = True

    while len(course) > 0:
        node = course.pop(0)
        D = distance.pop(0)
        for n in friend[node]:
            if not visit[n]:
                visit[n] = True
                distance += [D + 1]
                course += [n]
    if Min > D:
        Min = D
        candidate = [i]

    elif Min == D:
        candidate += [i]

print(Min, len(candidate))
for i in candidate:
    print(i)