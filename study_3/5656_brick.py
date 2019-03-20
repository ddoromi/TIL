import sys
sys.stdin = open('5656.txt')

T = int(input())
for test_case in range(1, T + 1):
    N, W, H = map(int, input().split())
    brick = []
    for h in range(H):
        brick.append(list(map(int, input().split())))
