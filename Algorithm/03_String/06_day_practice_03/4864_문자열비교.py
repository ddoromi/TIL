import sys
sys.stdin = open('4864.txt')

T = int(input())

for test_case in range(T):
    p = str(input())
    t = str(input())
    i = j = 0
    
    while j < len(p) and i < len(t):
        if p[j] == t[i]:
            i += 1
            j += 1
        else:
            i = i - j + 1
            j = 0 
            
    print(f'#{test_case+1}', end=' ')
    
    if j == len(p):
        print(1)
    else:
        print(0)
