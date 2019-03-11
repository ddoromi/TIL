import sys
sys.stdin = open('5110.txt')

T = int(input())
for test_case in range(1, T+1):
    N, M = map(int, input().split())
    data = list(map(int, input().split()))
    nums = []

    for i in range(M - 1):
        nums.append(list(map(int, input().split())))

    for i in range(M - 1):
        check = False
        for j in range(N):
            if data[j] > nums[i][0]:
                index = j
                check = True
                break

        if not check:
            for k in range(N):
                data.append(nums[i][k])
        else:
            for k in range(N):
                data.insert(index, nums[i][k])
                index += 1

    print('#{}'.format(test_case), end=' ')
    for i in range(1, 11):
        print(data[-i], end=' ')
    print()

