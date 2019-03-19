G = [[], [], [6], [2, 4, 5], [], [7], [], []]


def find_route(start, k=0):
    if k == 0:
        print(start, end=" ")
    for D in G[start]:
        print("------", D, end=" ")
        find_route(D, k+1)
        p

check_root = [i for i in range(1, 8)]


for node in G:
    for number in node:
        if number in check_root:
            check_root.pop(check_root.index(number))

for number in check_root:
    if len(G[number]) == 0:
        check_root.pop(check_root.index(number))


find_route(3)