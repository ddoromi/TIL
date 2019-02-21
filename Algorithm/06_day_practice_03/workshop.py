import sys
sys.stdin = open('workshop.txt')


for t in range(10):
    test_case = int(input())
    data = []
    Max, j = 0, 1
    
    for i in range(100):
        data.append(input())
    
    for m in range(100):
        while j <= 100:
            for i in range(100-j+1):
                text = data[m][i:i+j]
                if i==83 and j == 17:
                    print(text, text[::-1])
                if text[::-1] == text:
                    print(Max, len(text))
                    if Max < len(text):
                        Max = len(text)
            j += 1
   
    j = 1
    for m in range(100):
        while j <= 100:
            for i in range(100-j+1):
                text = ''
                for n in range(i, i+j):
                    text += data[n][m]
                if text[::-1] == text:
                    if Max < len(text):
                        Max = len(text)
            j += 1

    print(f'#{t+1} {Max}')

    