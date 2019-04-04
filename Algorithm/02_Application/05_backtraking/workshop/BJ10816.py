import sys
sys.stdin = open('BJ10816.txt')


def search_card(target, have2):
    start = 0
    end = len(have2) - 1
    while start <= end:
        mid = (start + end) // 2
        if target == have2[mid][0]:
            return have2[mid][1]
        elif target < have2[mid][0]:
            end = mid - 1
        else:
            start = mid + 1
    return 0

N = int(input())
have = list(map(int, input().split()))
M = int(input())
search = list(map(int, input().split()))
have.sort()

count = 1
have2 = []
for i in range(N):
    if i < N - 1 and have[i] == have[i + 1]:
        count += 1
    else:
        have2.append([have[i], count])
        count = 1

for i in range(M):
    search[i] = search_card(search[i], have2)

for i in search:
    print(i, end=' ')