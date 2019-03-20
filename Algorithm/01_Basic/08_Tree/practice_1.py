import sys
sys.stdin = open('tree_input.txt')


# 1. 트리의 높이를 계산하는 함수
def tree_height(v, height):
    global Max
    if v == 0:
        if height > Max:
            Max = height
        return

    height += 1
    tree_height(L[v], height)
    tree_height(R[v], height)


# # 2. 높이가 3인 노드를 출력하시오
def height_3(v, height):
    global Max
    if v == 0:
        return

    height += 1
    if height == 3:
        print(v, end=' ')
    height_3(L[v], height)
    height_3(R[v], height)


# # 3. 3번 노드가 루트인 트리의 전체 노드 수
def route_3(v):
    global count
    if v == 0: return

    count += 1
    route_3(L[v])
    route_3(R[v])


# # 4. 8번 노드와 10번 노드의 공통 조상을 출력하시오


V, E = map(int, input().split())
arr = list(map(int, input().split()))
L = [0] * (V + 1)
R = [0] * (V + 1)
P = [0] * (V + 1)
Max = 1

for i in range(0, E * 2, 2):
    u, v = arr[i], arr[i + 1]

    if L[u] == 0:
        L[u] = v
    else:
        R[u] = v
    P[v] = u


tree_height(1, -1)
print(Max)
height_3(1, -1)
print()

count = -1
route_3(3)
print(count)