import sys
sys.stdin = open('4831.txt')

T = int(input())

for t in range(T):
    Max, End, Num = map(int, input().split())
    Nums = list(map(int, input().split()))
    # stops = [0]
    count = 0
    idx = 0
    
    print(Max, End, Num, Nums)
    # # 정류장 리스트
    # for i in range(End+1):
    #     stops.append(i)
    
    for i in range(len(Nums)):

        if Nums[i-1] - Nums[i] > Max:
            break
            
        for j in range(End+1):
            if j == Nums[i]:
                if i == len(Nums)-1:
                    if Nums[i] - End > Max:
                        count += 1    
                        break
                if Nums[i+1]-idx > Max:
                    count += 1
                    idx = j

    print(f'#{t+1} {count}')