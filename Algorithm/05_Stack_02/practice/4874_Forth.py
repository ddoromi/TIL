import sys
sys.stdin = open('4864.txt')

T = int(input())
operator = ['+', '-', '*', '/']

for test_case in range(T):
    expression = input().split()
    stack = []

    for i in range(len(expression)):
        if expression[i] == '.':
            if len(stack) > 1:
                result = 'error'
                break
        elif not expression[i] in operator:
            stack.append(int(expression[i]))
        elif expression[i] in operator:
            if len(stack) < 2:
                result = 'error'
                break
            if expression[i] == '+':
                result = stack.pop(-2) + stack.pop(-1)
                stack.append(result)
            elif expression[i] == '-':
                result = stack.pop(-2) - stack.pop(-1)
                stack.append(result)
            elif expression[i] == '*':
                result = stack.pop(-2) * stack.pop(-1)
                stack.append(result)
            elif expression[i] == '/':
                result = stack.pop(-2) // stack.pop(-1)
                stack.append(result)
    if len(stack) == 0:
        result = 'error'
    print(f'#{test_case+1} {result}')
