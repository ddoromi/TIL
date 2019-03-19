import sys
sys.stdin = open('5653.txt')

T = int(input())
for test_case in range(1, T + 1):
    N, M, K = map(int, input().split())

    for i in range(N):
