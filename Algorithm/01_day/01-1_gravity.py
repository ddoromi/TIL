arr = [7, 4, 2, 0, 0, 6, 0, 7, 0]

max_h = 0  # max 낙차

for i in range(len(arr)):
    height = len(arr) - i
    cnt = 0  
    
    # i보다 크거나 같은 원소의 개수
    for j in range(i+1, len(arr)):
        if arr[i] <= arr[j]:
            cnt += 1
        
    height -= cnt
    max_h = max(height, max_h)

print (max_h)
print(len(arr))