cnt = 0
bit = [0] * 3  # 비트 표현 가능


def printHello(i, n):
    global cnt
    if i == n:
        print(bit)
        return
    bit[i] = 1
    printHello(i+1, n)
    bit[i] = 0
    printHello(i+1, n)

printHello(0, 3)


memo = [0] * 101


def fibo(n):
    if n < 2: return n
    if memo[n] != 0:
        return memo[n]
    else:
        memo[n] = fibo(n-1) + fibo(n-2)
        return memo[n]

print(fibo(40))

memo = [0] * 101
memo[0] = 0
memo[1] = 1

# 이미 memo는 값으로 차있다고 가정하고 값을 가져옴
for i in range(2, 41):
    memo[i] = memo[i - 1] + memo[i - 2]

print(memo[40])