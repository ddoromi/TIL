import sys
sys.stdin = open('5247.txt')
from collections import deque

T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    cal = deque([N])
    count = deque([0])
    visit = [False] * (M + 2)
    while len(cal):
        num = cal.popleft()
        cnt = count.popleft()
        if num == M:
            print('#{} {}'.format(test_case, cnt))
            break
        for xy in [num + 1, num - 1, num * 2, num - 10]:
            if 0 < xy < M + 2 and not visit[xy]:
                visit[xy] = True
                cal.append(xy)
                count.append(cnt + 1)

