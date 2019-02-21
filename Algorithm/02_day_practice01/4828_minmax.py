import sys
sys.stdin = open('4828.txt') 

T = int(input())
for t in range(T):
    N  = int(input())
    nums = list(map(int, input().split()))
    min_num, max_num = nums[0], nums[0]

    for i in range(N):
        if nums[i] > max_num:
            max_num = nums[i]
        if nums[i] < min_num:
            min_num = nums[i]

    print(f'#{t+1}', max_num - min_num)
            
            
            
