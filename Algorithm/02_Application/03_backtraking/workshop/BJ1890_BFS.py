import sys
from collections import deque
sys.stdin = open('BJ1890.txt')

N = int(input())
board = []
count = 0
for i in range(N):
    board.append(list(map(int, input().split())))
location = deque()
location.append([0, 0])

while len(location):
    index = location.popleft()
    if board[index[0]][index[1]] == 0:
        count += 1
    else:
        if index[0] + board[index[0]][index[1]] < N:
            location.append([index[0] + board[index[0]][index[1]], index[1]])
        if index[1] + board[index[0]][index[1]] < N:
            location.append([index[0], index[1] + board[index[0]][index[1]]])
print(count)