import sys
sys.stdin = open('2294.txt')

def coinChange(n):
    memo = [0] * (n + 1)

    for money in range(1, n + 1):
        MIN = 0xfffffff
        for i in range(len(coin)):
            if coin[i] > money:
                continue
            MIN = min(MIN, memo[money - coin[i]] + 1)
        memo[money] = MIN
    return memo

N, K = map(int, input().split())
coin = []
for i in range(N):
    coin.append(int(input()))

arr = coinChange(K)
if arr[K] == 0xfffffff:
    arr[K] = -1
print(arr[K])


