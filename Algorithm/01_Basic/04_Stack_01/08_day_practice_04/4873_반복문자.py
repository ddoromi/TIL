import sys
sys.stdin = open('4873.txt')

T = int(input())
for t in range(T):
    S = input()
    stack = []

    for i in range(len(S)):
        if len(stack) == 0 or stack[-1] != S[i]:
            stack.append(S[i])
        else:
            stack.pop(-1)

    print(f'#{t+1}', len(stack))
