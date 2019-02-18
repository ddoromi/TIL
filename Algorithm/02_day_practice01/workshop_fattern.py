import sys
sys.stdin = open('flatten_input.txt')

dump = int(input())
arr = list(map(int, input().split()))
cnt = [0] * 101
MinIdx, MaxIdx = 0, 100

for i in range(dump):
    while cnt[MinIdx] == 0:
        MinIdx += 1
    while cnt[MaxIdx] == 0:
        MaxIdx -= 1
    
    cnt[MinIdx] -= 1
    cnt[MinIdx+1] += 1
    cnt[MaxIdx] -= 1
    cnt[MaxIdx-1] += 1