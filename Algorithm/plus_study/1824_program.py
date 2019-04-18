import sys
sys.stdin = open('1824.txt')
from collections import deque

T = int(input())
for test_case in range(1, T + 1):
    R, C = map(int, input().split())
    data = []
    for i in range(R):
        data.append(list(input()))
    result = 'NO'
    memory = i = j = 0
    course = deque([[i, j]])
    while len(course):
        X, Y = course.popleft()
        direction = {'<': [X, Y - 1], '>': [X, Y + 1], '^': [X - 1, Y], 'v': [X + 1, Y]  }