import sys 
from IPython import embed

sys.stdin = open('input.txt', 'r') 
# sys.stdout = open('output.txt', 'w') 


for test in range(10):
    
    max_sum = 0
    data = []
    T = int(input())

    for i in range(100):
        data.append(list(map(int, input().split())))

    # 행 연산
    sum_cr, sum_cl, sum_max = 0, 0, 0
    for i in range(100):
        sum_cr += data[i][i]
        sum_cl += data[i][-i-1]
        
        sum_x, sum_y = 0, 0
        for j in range(100):
            sum_x += data[i][j]
            sum_y += data[j][i]
        
        if sum_max < sum_x:
            sum_max = sum_x
        if sum_max < sum_y:
            sum_max = sum_y
        
    max_sum = max(sum_max, sum_cr, sum_cl)

    print(f'#{T} {max_sum}')
