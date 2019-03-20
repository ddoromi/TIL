import sys
sys.stdin = open('1289.txt')

T = int(input())
for test_case in range(1, T + 1):
    memory = list(input())
    N = len(memory)
    init = [0 for _ in range(N)]
    count = 0

    for i in range(N):
        memory[i] = int(memory[i])

    for i in range(N):
        if memory[i] != init[i]:
            for j in range(i, N):
                init[j] = (init[j] + 1) % 2
            count += 1

    print('#{} {}'.format(test_case, count))
