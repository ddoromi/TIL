import sys
sys.stdin = open('5207.txt')


def binary_search(target, A):
    start, end = 0, N - 1
    left_check = False
    right_check = False
    while start <= end:
        mid = (start + end) // 2
        if A[mid] == target:
            return 1
        if A[mid] > target:
            if not left_check:
                left_check = True
                right_check = False
            else:
                return 0
            end = mid - 1
        else:
            if not right_check:
                right_check = True
                left_check = False
            else:
                return 0
            start = mid + 1
    return 0

T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    A.sort()
    count = 0
    for i in range(M):
        count += binary_search(B[i], A)
    print('#{} {}'.format(test_case, count))