import sys
sys.stdin = open('4837.txt')

T = int(input())

for t in range(T):
    data = list(map(int, input().split()))
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    sum_data = data[1]
    count = 0
    
    for i in range(1<<len(arr)):
        sum_arr = 0
        subset =[]
        
        for j in range(len(arr)):
            if i & (1<<j):
                sum_arr += arr[j]
                subset.append(arr[j])
        if len(subset) == data[0] and sum_arr == sum_data:
            count += 1
            
    print(f'#{t+1} {count}')




