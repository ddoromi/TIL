from IPython import embed

arr = [[9, 20, 2, 18, 11],
        [19, 1, 25, 3, 21],
        [8, 24, 10, 17, 7],
        [15, 4, 16, 5, 6],
        [12, 13, 22, 23, 14]]

result = 0
cal = [abs(arr[i][j]-arr[i-1][j]), abs(arr[i][j]-arr[i+1][j]), abs(arr[i][j]-arr[i][j-1]), abs(arr[i][j]-arr[i][j+1])]

for i in range(len(arr)):
    for j in range(len(arr[i])):
        if i == 0:
            if j == 0:
                result += result + abs(arr[i][j] - arr[i][j+1]) + abs(arr[i+1][j])
            else:
                result += result + abs(arr[i][j]-arr[i-1][j]) + abs(arr[i][j]-arr[i+1][j]) + abs(arr[i][j]-arr[i+1][j])

        elif i == len(arr) - 1:
            if j == len(arr[i])-1:
                result += result + abs(arr[i][j] - arr[i][j+1]) + abs(arr[i-1][j])
            else:
                result += result + abs(arr[i][j]-arr[i-1][j]) + abs(arr[i][j]-arr[i+1][j]) + abs(arr[i][j]-arr[i-1][j])





