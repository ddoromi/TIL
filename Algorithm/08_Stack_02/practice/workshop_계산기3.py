import sys
sys.stdin = open('workshop.txt')

for test_case in range(10):
    N = int(input())
    expression = list(input())
    
    for i in range(N):
        if expression[i] == []