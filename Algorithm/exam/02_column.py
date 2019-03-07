import sys
sys.stdin = open('02.txt')

T = int(input())
for test_case in range(T):
    words = []
    Max = 0
    result = ''

    for i in range(5):
        word = list(input())
        words.append(word)
        if len(word) > Max:
            Max = len(word)

    for i in range(5):
        words[i] += [0] * (Max - len(words[i]))

    for j in range(Max):
        for i in range(5):
            if words[i][j]:
                result += str(words[i][j])

    print('#{} {}'.format(test_case + 1, result))