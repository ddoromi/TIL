import sys
sys.stdin = open('5204.txt')

def merge_sort(low, high):
    global count
    if low + 1 == high: return nums[low]
    mid = (low + high) >> 1
    left = merge_sort(low, mid)
    right = merge_sort(mid, high)
    print(left, right)
    if left > right:
        count += 1
        return left
    else:
        return right
    # return merge(left, right)

# def merge(left, right):
#     global count
#     result = []
#     print(left, right)
#     if left[-1] > right[-1]:
#         count += 1
#     while len(left) > 0 and len(right) > 0:
#         if left[0] <= right[0]:
#             result.append(left.pop(0))
#         else:
#             result.append(right.pop(0))
#     if len(left) > 0:
#         result.extend(left)
#     if len(right) > 0:
#         result.extend(right)
#     return result

arr = [i for i in range(8)]
sorted = []

def mergesort(lo, hi):
    print(lo, hi)
    if lo == hi: return
    mid = (lo + hi) >> 1

    mergesort(lo, mid)
    mergesort(mid + 1, hi)
    i, j, k = lo, mid + 1, lo

    while i <= mid and j <= hi:
        if arr[i] < arr[j]:
            sorted[k] = arr[i]
            k, i = k + 1, i + 1
        else:
            sorted[k] = arr[j]
            k, j = k + 1, j + 1
    while i <= mid:
        sorted[k] = arr[i]
        k, j = k + 1, j + 1

    for i in range(lo, hi + 1):
        arr[i] = sorted[i]

def mergeSort(lo, hi):
    global ans
    if lo + 1 == hi: return arr[lo]
    mid = (lo + hi) >> 1

    l = mergesort(lo, mid)
    r = mergesort(mid, hi)
    if l > r:
        ans += 1
        return l
    else:
        return r

def quick_sort(arr, lo, hi, kth):
    j = lo - 1
    while kth != j:
        i, j = lo, hi
        while i <= hi and arr[i] <= arr[lo]:
            i += 1
        while arr[j] > arr[lo]:
            j -= 1
        if i >= j: break

        arr[i], arr[j] = arr[j], arr[i]
    arr[lo], arr[j] = arr[j], arr[lo]
    if ...
