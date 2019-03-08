import sys
sys.stdin = open('6190.txt')

T = int(input())
for test_case in range(T):
    N = int(input())
    nums = list(map(int, input().split()))
    Max = 0

    for i in range(N - 1):
        for j in range(i+1, N):
            num = nums[i] * nums[j]
            compare = []
            plus = False

            while num:
                compare.append(num % 10)
                num //= 10

            for l in range(len(compare) - 1):
                if compare[l] >= compare[l+1]:
                    plus = True
                else:
                    plus = False
                    break

            if len(compare) == 1 or plus:
                Max = max(Max, nums[i] * nums[j])

    if Max > 0:
        print('#{} {}'.format(test_case + 1, Max))
        continue
    print('#{} -1'.format(test_case + 1))