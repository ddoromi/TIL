K = int(input())
if K == 1:
    count = [[0, 1]]
else:
    count = [[0, 1], [1, 1]]
    for i in range(2, K):
        count.append([count[i-2][0]+count[i-1][0], count[i-2][1]+count[i-1][1]])

print(count[-1][0], count[-1][1])
