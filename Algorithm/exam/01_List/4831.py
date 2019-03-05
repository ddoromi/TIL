import sys
sys.stdin = open('4831.txt')

T = int(input())
for test_case in range(T):
    K, N, M = map(int, input().split())
    data = list(map(int, input().split()))
    charge = [0] * (N + 1)
    start = count = 0
    j = K

    for i in range(M):
        charge[data[i]] = 1

    while start <= N:
        if start + j >= N:
            break
        elif charge[start+j] == 1:
            count += 1
            start = start+j
            j = K
        else:
            j = j - 1
            if j == 0:
                count = 0
                break

    print('#{} {}'.format(test_case + 1, count))
