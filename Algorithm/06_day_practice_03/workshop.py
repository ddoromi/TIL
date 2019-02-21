import sys
sys.stdin = open('workshop.txt')


for t in range(10):
    test_case = int(input())
    data = []
    data_column = []
    Max, j = 1, 1
    
    for i in range(100):
        data.append(list(input()))
    
    for i in range(100):
        arr = []
        for j in range(100):
            arr.append(data[j][i])
        data_column.append(arr)
    
    for n in range(100):
        for j in range(2, 100):
            for i in range(100-j+1):
                text = data[n][i:i+j]
                text_column = data_column[n][i:i+j]

                if text == text[::-1]:
                    Max = max(Max, len(text), len(text_column))
                if text_column == text_column[::-1]:
                    Max = max(Max, len(text), len(text_column))
    
    print(f'#{t+1} {Max}')