import sys
sys.stdin = open('input.txt')

for N in range(10):
    T = int(input())
    data = list(map(int, input().split()))
    max_height, min_height, max_index, min_index = 1, 100, 0, 0

    for t in range(T):
        for i in range(len(data)):    
            if max_height <= data[i]:
                max_height = data[i]s
                max_index = i
                max_count = True
            
            if min_height >= data[i]:
                min_height = data[i]s
                min_index = i
                min_count = True
        
        data[max_index] -= 1ss
        data[min_index] += 1

        
        max_height -= 1
        min_height += 1

        if not max_count:
            for i in range(len(data)):    
                if max_height <= data[i]:
                    max_height = data[i]
                
                if min_height >= data[i]:
                    min_height = data[i]
                
        if data[max_index] - data[min_index] <= 1:
            break
        
    print (f'#{N+1} {data[max_index]-data[min_index]}')