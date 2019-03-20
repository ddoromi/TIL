import sys
sys.stdin = open('2005.txt')

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    triangle = [[0], [1], [1, 1], [1, 2, 1]]

    if N > 3:
        for i in range(4, N + 1):
            nums = [1 for _ in range(i)]
            for j in range(1, i // 2):
                nums[j] = nums[-j - 1] = (triangle[-1][j - 1] + triangle[-1][j])
            if i % 2:
                nums[i//2] = (triangle[-1][i//2 - 1] + triangle[-1][i//2])
            triangle.append(nums)

    print('#{}'.format(test_case))
    for i in range(1, N + 1):
        for j in triangle[i]:
            print(j, end=' ')
        print()