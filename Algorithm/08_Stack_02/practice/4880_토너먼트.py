import sys
sys.stdin = open('4880.txt')


def getmax(start, end):
    if start == end:
        return player[start], start
    mid = (start + end) >> 1
    left, left_idx = getmax(start, mid)
    right, right_idx = getmax(mid + 1, end)

    if (left == right) or (left == 1 and right == 3) or (left == 2 and right == 1) or (left == 3 and right == 2):
        return left, left_idx
    else:
        return right, right_idx


T = int(input())

for test_case in range(T):
    N = int(input())
    player = list(map(int, input().split()))

    print(f'#{test_case + 1} {getmax(0, len(player) - 1)[1] + 1}')