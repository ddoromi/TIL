coin = [6, 4, 1]
ans = 0xffff
path = [0] * 100

def coinChange(k, n):
    global ans
    if k >= ans: return
    if n == 0:
        ans = min(ans, k)
        print(path[0: k])
        return

    for val in coin:
        if val > n:
            continue
        path[k] = val
        coinChange(k + 1, n - val)
coinChange(0, 80)
print(ans)


def coinChange2(k, n):
    if n == 0: return 0
    MIN = 0xffff
    for val in coin:
        if val > n:
            continue
        ret = coinChange(n - val)
        MIN = min(MIN, ret)
    return MIN + 1

print(coinChange2(8))