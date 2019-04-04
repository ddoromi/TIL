w = [0, 3, 4, 5, 6]  # 1 ~ N번 물건의 무게
v = [0, 50, 40, 10, 30]  # 1 ~ N번 물건의 가치
maxW, maxV = 10, 0
N = len(v)

def knapsack(k, W, curV):
    global maxV
    if k == 0:
        maxV = max(maxV, curV)
        print('최대 가치 =', maxV)
        return
    if W >= w[k]:
        knapsack(k - 1, W - w[k], curV + v[k])
    knapsack(k - 1, W, curV)

knapsack(N - 1, maxW, 0)

def knapsack2(k, W):
    if k == 0 or w == 0:
        return
    if W >= w[k]:
        case1 = knapsack2(k - 1, W - w[k]) + v[k]
    case2 = knapsack2(k - 1, W)
    return case1 if case1 > case2 else case2
print(knapsack2(N, maxW))