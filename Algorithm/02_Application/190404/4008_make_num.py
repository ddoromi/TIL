import sys
sys.stdin = open('4008.txt')

def make_nums(k, n, Sum):
    global Max, Min
    if k == n:
        Max = max(Max, Sum)
        Min = min(Min, Sum)
    for i in range(4):
        if operator[i] > 0:
            operator[i] -= 1
            if i == 0:
                make_nums(k + 1, n, Sum + nums[k + 1])
            elif i  == 1:
                make_nums(k + 1, n, Sum - nums[k + 1])
            elif i  == 2:
                make_nums(k + 1, n, Sum * nums[k + 1])
            else:
                if Sum < 0:
                    make_nums(k + 1, n, -(-Sum // nums[k + 1]))
                else:
                    make_nums(k + 1, n, Sum // nums[k + 1])
            operator[i] += 1

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    operator = list(map(int, input().split()))
    nums = list(map(int, input().split()))
    Min, Max = 10000000, -100000000
    make_nums(0, N - 1, nums[0])
    print('#{} {}'.format(test_case, Max - Min))