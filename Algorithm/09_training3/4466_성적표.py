import sys
sys.stdin = open('4466.txt')

T = int(input())
for test_case in range(1, T + 1):
    N, K = map(int, input().split())
    subjects = list(map(int, input().split()))
    Sum = 0
    for i in range(N):
        Max = subjects[i]
        index = i
        for j in range(i, N):
            if Max < subjects[j]:
                Max = subjects[j]
                index = j
        subjects[i], subjects[index] = subjects[index], subjects[i]
    for i in range(K):
        Sum += subjects[i]
    print('#{} {}'.format(test_case, Sum))