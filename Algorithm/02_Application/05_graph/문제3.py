T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    farm = []
    for j in range(N):
        farm.append([])
    for p in range(N):
        for _ in range(N):
            farm[p].append(0)
    rabbit = []
    for _ in range(M):
        li = list(map(int, input().split()))
        rabbit.append(li)
    for i in range(M):
        if rabbit[i][2] == 0:
            farm[rabbit[i][0]][rabbit[i][1]] += 1
            while rabbit[i][0] >= 0:
                rabbit[i][0] -= rabbit[i][3]
                if rabbit[i][0] < 0:
                    break
                else:
                    farm[rabbit[i][0]][rabbit[i][1]] += 1
        if rabbit[i][2] == 1:
            farm[rabbit[i][0]][rabbit[i][1]] += 1
            while rabbit[i][0] <= N - 1:
                rabbit[i][0] += rabbit[i][3]
                if rabbit[i][0] > N-1:
                    break
                else:
                    farm[rabbit[i][0]][rabbit[i][1]] += 1
        if rabbit[i][2] == 2:
            farm[rabbit[i][0]][rabbit[i][1]] += 1
            while rabbit[i][1] >= 0:
                rabbit[i][1] -= rabbit[i][3]
                if rabbit[i][1] < 0:
                    break
                else:
                    farm[rabbit[i][0]][rabbit[i][1]] += 1
        if rabbit[i][2] == 3:
            farm[rabbit[i][0]][rabbit[i][1]] += 1
            while rabbit[i][1] <= N - 1:
                rabbit[i][1] += rabbit[i][3]
                if rabbit[i][1] > N-1:
                    break
                else:
                    farm[rabbit[i][0]][rabbit[i][1]] += 1
    m = []
    ans = 0
    for k in range(N):
        m.append(max(farm[k]))
    realm = max(m)
    for l in range(N):
        for o in range(N):
           if farm[l][o] == realm:
               ans += 1
    print("#"+str(tc), realm, ans)

