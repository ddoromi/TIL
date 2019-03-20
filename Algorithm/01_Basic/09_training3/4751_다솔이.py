import sys
sys.stdin = open('4751.txt')

T = int(input())
for test_case in range(1, T + 1):
    string = input()
    N = len(string)
    result = ['' for _ in range(5)]
    result[2] = '#'
    result[0] = result[4] = '.' + '.#..' * N
    result[1] = result[3] = '.' + '#.' * N * 2

    for i in range(N):
        result[2] += '.' + string[i] + '.#'

    for i in range(5):
        print(result[i])
