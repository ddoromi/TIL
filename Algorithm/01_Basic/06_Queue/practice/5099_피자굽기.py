import sys
sys.stdin = open('5099.txt')

def isEmpty(array):
    global count, j
    if len(array) > 0:
        j += 1
        return [j] + [array.pop(0)]
    else:
        count -= 1
        return False


T = int(input())
for test_case in range(T):
    N, M = map(int, input().split())
    C = list(map(int, input().split()))
    count = N
    oven = []
    j = 0

    for i in range(N):
        j += 1
        oven.append([j] + [C.pop(0)])

    while count > 1:
        for i in range(N):
            if oven[i]:
                oven[i][1] //= 2
                if oven[i][1] == 0:
                    oven[i] = isEmpty(C)

            if count == 1:
                break

    for i in range(N):
        if oven[i]:
            print('#{} {}'.format(test_case + 1, oven[i][0]))