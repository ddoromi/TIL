import sys
sys.stdin = open('01.txt')

T = int(input())
for test_case in range(T):
    N, K = map(int, input().split())
    fruits = []
    Min = 0xffff

    for i in range(N):
        fruits.append(list(map(int, input().split())))

    # if K % 2:
    #     count = (K - 1)//2
    #     for i in range(count, N - count):
    #         for j in range(count, N - count):
    #             right_sum = left_sum = fruits[i][j]
    #
    #             for k in range(1, count + 1):
    #                 right_sum = right_sum + fruits[i-k][j-k] + fruits[i+k][j+k]
    #                 left_sum = left_sum + fruits[i+k][j-k] + fruits[i-k][j+k]
    #
    #             Min = min(Min, abs(right_sum - left_sum))

    # else:
    for i in range(N - K + 1):
        for j in range(N - K + 1):
            right_sum = left_sum = 0
            index = (j + K) - 1
            for k in range(K):
                right_sum = right_sum + fruits[i+k][j+k]
                left_sum = left_sum + fruits[i+k][index-k]

            Min = min(Min, abs(right_sum - left_sum))

    print('#{} {}'.format(test_case + 1, Min))





