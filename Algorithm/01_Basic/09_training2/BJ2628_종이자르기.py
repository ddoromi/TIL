import sys
sys.stdin = open('BJ2628.txt')

width, height = map(int, input().split())
N = int(input())
row = [0]
column = [0]
row_max = column_max = 0

for i in range(N):
    d, num = map(int, input().split())
    if d == 0:
        column += [num]
    else:
        row += [num]

row += [width]
column += [height]
row.sort()
column.sort()

for i in range(len(row) - 1):
    if row[i + 1] - row[i] > row_max:
        row_max = row[i + 1] - row[i]

for i in range(len(column) - 1):
    if column[i + 1] - column[i] > column_max:
        column_max = column[i + 1] - column[i]

print(row_max * column_max)


