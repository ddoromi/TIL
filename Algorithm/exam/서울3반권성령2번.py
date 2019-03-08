import sys
sys.stdin = open('02.txt')

# T = int(input())
# for test_case in range(T):
#     N = int(input())
#     island = []
#     data = [[0 for _ in range(N)]]
#     num_island = Max = 0
#
#     for i in range(N):
#         data.append(list(map(int, input().split())))
#
#     i = j = 0
#     while 1 <= i < N-1:
#         be = False
#         if j == (N - 1):
#             i += 1
#
#         if data[i-1][j] == 0 and data[i][j] > 0:
#             i_index, j_index, count = i, j, 0
#             num_island += 1
#
#             for k in range(N):
#                 if i_index + k == N:
#                     break
#
#                 for l in range(N):
#                     be = False
#                     if data[i_index+k][j_index+l] == 0 or j_index + l == N - 1:
#                         i += 1
#                         j = 0
#                         break
#                     else:
#                         Max = max(Max, data[i_index+k][j_index+l])
#                         count += 1
#                         j = count
#                         be = True
#         if not be:
#             j += 1
#
#
#     print('#{} {} {}'.format(test_case + 1, num_island, Max))

for t in range(int(input())):
    size = int(input())
    cnt = height = 0
    MAP = []
    for _ in range(size):
        MAP.append(list(map(int, input().split())))

    island = [[False] * size for _ in range(size)]

    for row in range(size):
        for col in range(size):
            if MAP[row][col] == 0:
                continue

            if MAP[row][col] > height:
                height = MAP[row][col]

            island[row][col] = True
            cnt += 1
            if island[row - 1][col] or island[row][col - 1]:
                cnt -= 1

print("#{} {} {}".format(t + 1, cnt, height))