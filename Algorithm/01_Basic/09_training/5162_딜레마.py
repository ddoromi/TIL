import sys
sys.stdin = open('5162.txt')

T = int(input())
for test_case in range(1, T + 1):
    bread_1, bread_2, money = map(int, input().split())
    print('#{} {}'.format(test_case, money // min(bread_1, bread_2)))