import sys
sys.stdin = open('2382.txt')

T = int(input())
for test_case in range(1, T + 1):
    N, M, K = map(int, input().split())
    micro = []
    for i in range(K):
        micro.append(list(map(int, input().split())))
    for i in range(M):
        array = []
        for j in range(len(micro)):
            if micro[j][2] == 0:
                array.append(j)
        for j in range(1, len(array) + 1):
            micro.pop(array[-j])
        for mm in micro:
            if mm[2] != 0:
                direction = [[mm[0] - 1, mm[1]], [mm[0] + 1, mm[1]], [mm[0], mm[1] - 1], [mm[0], mm[1] + 1]]
                mm[0], mm[1] = direction[mm[3] - 1]
        for mm in micro:
            if mm[2] != 0 and (mm[0] in [0, N - 1] or mm[1] in [0, N - 1]):
                direction = [2, 1, 4, 3]
                mm[2], mm[3] = mm[2] // 2, direction[mm[3] - 1]
        visit = [False for _ in range(len(micro))]
        for m1 in range(len(micro)):
            if visit[m1]: continue
            same = []
            if micro[m1][2] != 0:
                same.append(m1)
            for m2 in range(len(micro)):
                if m1 == m2 or visit[m2]: continue
                if micro[m2][2] != 0 and ([micro[m1][0], micro[m1][1]] == [micro[m2][0], micro[m2][1]]):
                    same.append(m2)
            aa = []
            if len(same) > 1:
                Max = max(micro[i][2] for i in same)
                Sum = sum(micro[i][2] for i in same)
                for ss in same:
                    visit[ss] = True
                    if micro[ss][2] == Max:
                        micro[ss][2] = Sum
                    else:
                        micro[ss][2] = 0
                        aa.append(ss)
    print('#{} {}'.format(test_case, sum(micro[i][2] for i in range(len(micro)))))