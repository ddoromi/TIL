import sys
sys.stdin = open('5248.txt')

T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    data = list(map(int, input().split()))
    people = [[] for _ in range(N + 1)]
    for i in range(0, M * 2, 2):
        people[data[i]].append(data[i + 1])
        people[data[i + 1]].append(data[i])
    print(people)