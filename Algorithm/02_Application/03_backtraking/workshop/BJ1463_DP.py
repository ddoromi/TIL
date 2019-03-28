import sys
sys.stdin = open('BJ1463.txt')

N = int(input())
DP = [0] * (N + 1)
if N > 1:
    for i in range(2, N + 1):
        if i % 2 == 0 and i % 3 == 0:
            DP[i] = min(DP[i // 2], DP[i // 3], DP[i - 1]) + 1
        elif i % 2 == 0:
            DP[i] = min(DP[i // 2], DP[i - 1]) + 1
        elif i % 3 == 0:
            DP[i] = min(DP[i // 3], DP[i - 1]) + 1
        else:
            DP[i] = DP[i - 1] + 1
print(DP[N])

