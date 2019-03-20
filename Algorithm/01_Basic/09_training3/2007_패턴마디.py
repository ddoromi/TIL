import sys
sys.stdin = open('2007.txt')

T = int(input())
for test_case in range(1, T + 1):
    pattern = input()
    word = ''

    for i in range(2, 10):
        if pattern[0:i] == pattern[i:i*2]:
            break
    print('#{} {}'.format(test_case, i))