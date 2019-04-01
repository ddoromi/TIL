import sys
sys.stdin = open('5204.txt')

def merge_sort(low, high):
    global count
    if low + 1 == high: return nums[low]
    mid = (low + high) >> 1
    left = merge_sort(low, mid)
    right = merge_sort(mid, high)
    if left > right:
        count += 1
        return left
    else:
        return right

T = int(input())
for test_case in range(1, T + 1):
    count = 0
    N = int(input())
    nums = list(map(int, input().split()))
    merge_sort(0, N)
    nums.sort()
    print('#{} {} {}'.format(test_case, nums[N // 2], count))
