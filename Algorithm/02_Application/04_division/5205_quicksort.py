import sys
sys.stdin = open('5205.txt')


def quick_sort(nums):
    if len(nums) <= 1:
        return nums
    pivot = nums[len(nums) // 2]
    low, mid, high = [], [], []
    for num in nums:
        if num < pivot:
            low.append(num)
        elif num > pivot:
            high.append(num)
        else:
            mid.append(num)
    return quick_sort(low) + mid + quick_sort(high)


T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    data = list(map(int, input().split()))
    result = quick_sort(data)
    print('#{} {}'.format(test_case, result[N // 2]))
