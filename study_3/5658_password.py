import sys
sys.stdin = open('5658.txt')

T = int(input())
for test_case in range(1, T + 1):
    N, K = map(int, input().split())
    data = list(input())
    n = N // 4
    convert = {'A' : 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}
    nums = {}
    array = []
    for k in range(n):
        for i in range(0, N, n):
            check = ''
            for j in range(n):
                check += data[i + j]
            if check in nums:
                continue
            else:
                num = 0
                for j in range(n):
                    if check[j] in convert:
                        num += convert[check[j]] * (16 ** (n - 1 - j))
                    else:
                        num += int(check[j]) * (16 ** (n - 1 - j))
                nums[check] = num
                array.append(num)
        data.insert(0, data.pop())
    array.sort(reverse=True)
    print('#{} {}'.format(test_case, array[K - 1]))