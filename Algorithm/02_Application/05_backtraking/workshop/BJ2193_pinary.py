N = int(input())
if N < 3:
    print(1)
else:
    fibo = [0] * (N + 1)
    fibo[1] = fibo[2] = 1
    for i in range(3, N + 1):
        fibo[i] = fibo[i - 1] + fibo[i - 2]
    print(fibo[N])