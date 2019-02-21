import sys 
sys.stdin = open('input.txt')

T = int(input())

# Test Case
for t in range(T):
    N = int(input())   # 색칠할 영역의 개수
    data = list(map(int, input().split()))
    array = []   # arr = [[0 for _ in range(10)] for _ in range(10)]
    
    for i in range(0, len(data), 2):
        array += [[data[i], data[i+1]]]

    for i in range(len(array)):
        for j in range(len(array)):
            if j == i:
                pass
            if array[i][0] == array[j][1]:
                break
        else:
            array[i], array[0] = array[0], array[i]
    
    for i in range(1, len(array)):
        for j in range(i, len(array)):
            if array[i-1][1] == array[j][0]:
                array[i], array[j] = array[j], array[i]

    print (f'#{t+1}', end=' ')
    for i in range(len(array)):
        print(array[i][0], array[i][1], end=' ')
    print()
