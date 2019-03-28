import sys
sys.stdin = open('5202.txt')

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    truck = []
    for i in range(N):
        truck.append(list(map(int, input().split())))
    for i in range(N):
        Min, index = truck[i][1], i
        for j in range(i + 1, N):
            if truck[j][1] < Min:
                Min, index = truck[j][1], j
        truck[i], truck[index] = truck[index], truck[i]
    Max = 0
    for i in range(N):
        used = [truck[i]]
        for j in range(i + 1, N):
            if used[-1][1] - used[0][0] > 24:
                break
            if truck[j][0] >= used[-1][1]:
                used.append(truck[j])
        if Max < len(used):
            Max = len(used)
    print('#{} {}'.format(test_case, Max))
