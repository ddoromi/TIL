import sys
sys.stdin = open('2455.txt')

Max = train = 0
for i in range(4):
    off, on = map(int, input().split())
    train = train + on - off
    if train > Max:
        Max = train
print(Max)