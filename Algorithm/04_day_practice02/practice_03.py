data = [[9, 20, 2, 18, 11],
    [19, 1, 25, 3, 21],
    [8, 24, 10, 17, 7],
    [15, 4, 16, 5, 6],
    [12, 13, 22, 23, 14]]
data_sort = []
result = [[0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0]]

X = len(data[0])
Y = len(data)

for i in range(X):
    for j in range(Y):
        data_sort.append(data[i][j])

for i in range(len(data_sort)):
    Min = data_sort[i]
    MinIdx = i 
    
    for j in range(i, len(data_sort)):
        if Min > data_sort[j]:
            Min = data_sort[j]
            MinIdx = j
    
    data_sort[i], data_sort[MinIdx] = data_sort[MinIdx], data_sort[i]

n = 0
x = 0
y = 0

for j in range(Y):
    result[x][j] = data_sort[n]
    n += 1

for i in range(1, X):
    result[i][Y-1] = data_sort[n]
    n += 1

for j in range(Y-2, -1, -1):
    result[X-1][j] = data_sort[n]
    n += 1

for i in range(X-2, 0, -1):
    result[i][y] = data_sort[n]
    n += 1

for j in range(1, Y-1):
    result[X-4][j] = data_sort[n]
    n += 1

for i in range(2, X-1):
    result[i][Y-2] = data_sort[n]
    n += 1

for j in range(Y-3, 0, -1):
    result[X-2][j] = data_sort[n]
    n += 1

for j in range(1, Y-2):
    result[X-3][j] = data_sort[n]
    n += 1

print(result)
