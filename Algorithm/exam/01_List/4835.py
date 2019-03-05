import sys
sys.stdin = open('4835.txt')

T = int(input())
for test_case in range(T):
    N, M = map(int, input().split())
    nums = list(map(int, input().split()))
