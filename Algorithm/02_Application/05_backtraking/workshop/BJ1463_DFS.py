import sys
sys.setrecursionlimit(0xffffff)
sys.stdin = open('BJ1463.txt')

def make_own(N, count):
    global Min
    if N < 1:
        return
    if N == 1:
        Min = min(Min, count)
        return
    cal = [3, 2, -1]
    for c in cal:
        if c == -1:
            make_own(N - 1, count + 1)
        if N % c == 0:
            make_own(N // c, count + 1)

N = int(input())
Min = 0xfffff

make_own(N, 0)
print(Min)