import sys
sys.stdin = open('4834.txt')

T = int(input())
for test_case in range(T):
    N = int(input())
    data = input()
    nums = {}
    Max = 0

    for i in range(N):
        if int(data[i]) in nums:
            nums[int(data[i])] += 1
        else:
            nums[int(data[i])] = 1

    for key in nums:
        if nums[key] > Max:
            Max = nums[key]
            num = key
        if nums[key] == Max:
            if key > num:
                num = key

    print('#{} {} {}'.format(test_case+1, num, Max))



