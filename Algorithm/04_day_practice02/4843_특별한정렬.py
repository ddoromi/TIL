import sys
sys.stdin = open('4843.txt')

T = int(input())

for t in range(T):
    N = int(input())
    data = list(map(int, input().split()))

    for i in range(10):
        Max = data[i]
        Min = data[i]
        MaxIdx = i
        MinIdx = i
        if i%2 == 0:   
            for n in range(i+1, len(data)):
                if data[n] > Max:
                    Max = data[n]
                    MaxIdx = n
            data[i], data[MaxIdx] = data[MaxIdx], data[i]
        
        else:
            for n in range(i+1, len(data)):
                if data[n] < Min:
                    Min = data[n]
                    MinIdx = n
            data[i], data[MinIdx] = data[MinIdx], data[i]
    
    print(f'#{t+1}', end=' ')
    for i in range(10):
        print(f'{data[i]}', end=' ')
    print()
