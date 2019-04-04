import sys
sys.stdin = open('4408.txt')

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    rooms = []
    visit = [0] * 401
    for i in range(N):
        x, y = map(int, input().split())
        if x > y:
            x, y = y, x
        rooms.append([x, y])
    for i in range(N):
        before_s, before_e = rooms[i][0], rooms[i][1]
        if before_s % 2 == 0:
            before_s -= 1
        if before_e % 2:
            before_e += 1
        for i in range(before_s, before_e + 1):
            visit[i] += 1
    print('#{} {}'.format(test_case, max(visit)))



