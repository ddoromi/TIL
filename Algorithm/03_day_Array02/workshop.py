import sys 
from IPython import embed

sys.stdin = open('input.txt', 'r') 
# sys.stdout = open('output.txt', 'w') 


for test in range(10):
    
    data = []
    T = int(input())

    for i in range(100):
        data.append(list(map(int, input().split())))

    sum_cr, sum_cl, max_xy = 0, 0, 0
    
    for i in range(100):

        # 대각선 연산
        sum_cr += data[i][i]
        sum_cl += data[i][99-i]
        
        sum_x, sum_y = 0, 0
        for j in range(100):
            sum_x += data[i][j]
            sum_y += data[j][i]
        
        if sum_x > max_xy:
            max_xy = sum_x
        if sum_y > max_xy:
            max_xy = sum_y

    max_sum = max(max_xy, sum_cr, sum_cl)

    print(f'#{T} {max_sum}')

# 교수님 코드
# for test_case in range(1, 11):
#     N = int(input())
#     arr = []
#     for i in range(100):
#         arr.append(list(map(int, input().split())))

#     Max = diag1 = diag2 = 0
#     for i in range(100):
#         diag1 += arr[i][i]
#         diag2 += arr[i][99-i]
#         rsum = csum = 0
#         for j in range(100):
#             rsum += arr[i][j]
#             csum += arr[j][i]
#         Max = max(Max, rsum, csum)
#     Max = max(Max, diag1, diag2)
#     print(Max)