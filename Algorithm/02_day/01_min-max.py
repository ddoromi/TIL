import sys
sys.stdin = open('input.txt', 'r') 
sys.stdout = open('output.txt', 'w') 

T = int(input())
for i in range(T):
    N  = int(input())
    
    for j in range(N):
        nums = list(map(int, input.split()))
        min_num, max_num = nums[0], nums[0]

        for num in nums:
            if min_num > num:
                min_num = num
            if max_num < num:
                max_num = num

        print 
            
            
            
