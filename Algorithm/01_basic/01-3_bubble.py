arr = [55, 7, 78, 12, 42]

for j in range(1, len(arr)-1):
    for i in range(len(arr)-j):
        if arr[i] > arr[i+1]:
            arr[i], arr[i+1] = arr[i+1], arr[i]

print(arr)

