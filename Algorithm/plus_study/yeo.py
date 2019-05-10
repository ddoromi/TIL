import sys

sys.stdin = open('17140.txt')

X = []

dp = [0]*101
dp2=[0]*101

r, c = 0

for _ in range(4):
    X.append(list(map(int, input().split())))



for i in X:
    for j in i:
