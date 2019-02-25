import sys
sys.stdin = open('4588.txt')

brackets = {')': '(', '}': '{', ']': '['}
T = int(input())

for t in range(T):
    checked, j = [], 0
    test = list(input())

    while j < len(test):
        if test[j] in brackets.values():
            checked.append(test[j])
        elif test[j] in brackets.keys():
            if len(checked) == 0 or brackets[test[j]] != checked.pop(-1):
                print(f'#{t+1} 0')
                break
        if j == len(test) - 1:
            if len(checked):
                print(f'#{t+1} 0')
            else:
                print(f'#{t + 1} 1')
        j += 1