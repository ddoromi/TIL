import sys
sys.stdin = open('2636.txt')

row, column = map(int, input().split())
cheese_before = [[0] * (column + 2)]
cheese_after = []

for i in range(row):
    cheese_before.append([0] + list(map(int, input().split())) + [0])

cheese_before.append([[0] * (column + 2)])

print(cheese_before)
#
# for i in range(row):
#     for j in range(column)
