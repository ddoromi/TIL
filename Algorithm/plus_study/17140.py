import sys
sys.stdin = open('17140.txt')


def operator_R(MAP):
    for i in range(len(MAP)):
        nums = []
        visit = []
        for j in range(len(MAP[i])):
            if MAP[i][j] and MAP[i][j] not in visit:
                visit.append(MAP[i][j])
                nums.append([MAP[i][j], MAP[i].count(MAP[i][j])])
        for l in range(len(nums)):
            index, Min = l, nums[l][1]
            for m in range(l+1, len(nums)):
                if nums[m][1] < Min:
                    index, Min = m, nums[m][1]
            nums[index], nums[l] = nums[l], nums[index]

        for l in range(len(nums) - 1):
            index, Min = l, nums[l][1]
            for m in range(l+1, len(nums)):
                if nums[m][1] == Min and nums[index][0] > nums[m][0]:
                    index, Min = m, nums[m][1]
            nums[index], nums[l] = nums[l], nums[index]

        MAP[i] = []
        for num in nums:
            MAP[i].append(num[0])
            MAP[i].append(num[1])

    Max = max([len(MAP[i]) for i in range(len(MAP))])
    for i in range(len(MAP)):
        for j in range(Max - len(MAP[i])):
            MAP[i].append(0)


def operator_C(MAP):
    MAP2 = [[] for _ in range(len(MAP[0]))]
    for i in range(len(MAP[0])):
        nums = []
        visit = []
        for j in range(len(MAP)):
            if MAP[j][i] and MAP[j][i] not in visit:
                visit.append(MAP[j][i])
                cnt = 0
                for k in range(len(MAP)):

        for l in range(len(nums)):
            index, Min = l, nums[l][1]
            for m in range(l+1, len(nums)):
                if nums[m][1] < Min:
                    index, Min = m, nums[m][1]
            nums[index], nums[l] = nums[l], nums[index]

        for l in range(len(nums) - 1):
            index, Min = l, nums[l][1]
            for m in range(l+1, len(nums)):
                if nums[m][1] == Min and nums[index][0] > nums[m][0]:
                    index, Min = m, nums[m][1]
            nums[index], nums[l] = nums[l], nums[index]

        for num in nums:
            visit.append(num[0])
            visit.append(num[1])
        print(visit)
        MAP2[i] = visit

    # Max = max([len(MAP2[i]) for i in range(len(MAP2))])
    # for i in range(len(MAP2)):
    #     for j in range(Max - len(MAP2[i])):
    #         MAP2[i].append(0)
    #
    # print(MAP2)


for test_case in range(6):
    r, c, k = map(int, input().split())
    MAP = []
    count = 0
    result = 0
    for i in range(3):
        MAP.append(list(map(int, input().split())))

    for i in range(2):
        # if MAP[r][c] == k:
        #     result = count
        #     break
        if count > 100:
            result = -1
            break
        if len(MAP) >= len(MAP[0]):
            operator_R(MAP)
        else:
            operator_C(MAP)