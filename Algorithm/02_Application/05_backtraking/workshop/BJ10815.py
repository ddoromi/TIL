import sys
sys.stdin = open('BJ10815.txt')


def number_card(target, have):
    start = 0
    end = N - 1

    while start <= end:
        mid = (start + end) // 2
        if have[mid] == target:
            return 1
        elif have[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return 0


N = int(input())
have = list(map(int, input().split()))
M = int(input())
search = list(map(int, input().split()))
have.sort()

for i in range(M):
    search[i] = number_card(search[i], have)
for i in search:
    print(i, end=' ')

