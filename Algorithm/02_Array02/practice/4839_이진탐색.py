import sys
sys.stdin = open('4839.txt')

T = int(input())

for t in range(T):
    data = list(map(int, input().split()))
    A_start = B_start = 1
    A_end = B_end = data[0]
    A_middle = B_middle = int(data[0]+1/2)
    A_count = B_count = 1
    
    while A_middle != data[1]:
        if A_middle > data[1]:
            A_end = A_middle
        else:
            A_start = A_middle
        A_middle = int((A_start+A_end)/2)
        A_count += 1

    while B_middle != data[2]:
        if B_middle > data[2]:
            B_end = B_middle
        else:
            B_start = B_middle
        B_middle = int((B_start+B_end)/2)
        B_count += 1
    
    print(f'#{t+1}',end=' ')
    
    if A_count > B_count:
        print(f'B')
    elif A_count < B_count:
        print(f'A')
    else:
        print('0')