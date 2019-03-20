import sys
sys.stdin = open('input.txt', 'r') # 읽기 모드
# sys.stdout = open('output.txt', 'w') # 쓰기 모드

# for test_case in range(length):
#     N = int(input())
#     data = []
    
#     for  i in range(N):
#         data.append(list(map(int, input().split())))


# max 함수 사용
for j in range(10):
    length = int(input())
    data = list(map(int, input().split()))
    result = 0
    
    for i in range(2, len(data)-2):
        if data[i] > max(data[i-2], data[i-1], data[i+1], data[i+2]):
            result += data[i] - max(data[i-2], data[i-1], data[i+1], data[i+2])

    print(f'#{j+1} {result}')
    

# max를 직접 구해서
for k in range(10):
    length = int(input())
    data = list(map(int, input().split()))
    result = 0
    
    for i in range(2, len(data)-2):
        max_h = 0
        for j in [data[i-2], data[i-1], data[i+1], data[i+2]]:
            if max_h < j:
                max_h = j

        if data[i] > max_h:
            result += data[i] - max_h

    print(f'#{k+1} {result}')