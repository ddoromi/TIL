import sys
sys.stdin = open('2167.txt')

N, M = map(int, input().split())
nums, index = [], []
for i in range(N):
    nums.append(list(map(int, input().split())))

K = int(input())
for j in range(K):
    i, j, x, y = map(int, input().split())
    index.append([i - 1, j - 1, x - 1, y - 1])

for idx in index:
    Sum = 0
    for i in range(idx[0], idx[2] + 1):
        for j in range(idx[1], idx[3] + 1):
            Sum += nums[i][j]
    print(Sum)

