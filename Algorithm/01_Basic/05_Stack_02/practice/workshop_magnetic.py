import sys
sys.stdin = open('workshop.txt')

for test_case in range(10):
    table = []
    width = int(input())
    count = 0

    for i in range(100):
        table.append(list(map(int, input().split())))

    for x in range(len(table)):
        stack = []
        for y in range(len(table)):
            if len(stack) == 0:
                if table[y][x] == 1:
                    stack.append(1)
                continue
            if stack[-1] == 1 and table[y][x] == 2:
                stack.pop(-1)
                count += 1

    print(f'#{test_case+1} {count}')
