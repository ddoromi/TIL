import sys
sys.stdin = open('5248.txt')

def group(n):
    visit[n] = True
    for v in people[n]:
        if not visit[v]:
            group(v)

T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    data = list(map(int, input().split()))
    people = [[] for _ in range(N + 1)]
    visit = [False] * (N + 1)
    count = 0
    for i in range(0, M * 2, 2):
        people[data[i]].append(data[i + 1])
        people[data[i + 1]].append(data[i])
    for i in range(1, N + 1):
        if len(people[i]) and not visit[i]:
            group(i)
            count += 1
    for i in range(1, N + 1):
        if not visit[i]:
            count += 1
    print('#{} {}'.format(test_case, count))
