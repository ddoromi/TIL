import sys
sys.stdin = open('BJ9095.txt')
N = int(input())
for i in range(N):
    num = int(input())
    count = 0
    DP = [0] * (num + 1)
    DP[0] = 1
    for j in range(num + 1):
        if j - 1 >= 0:
            DP[j] += DP[j - 1]
        if j - 2 >= 0:
            DP[j] += DP[j - 2]
        if j - 3 >= 0:
            DP[j] += DP[j - 3]
    print(DP[j])