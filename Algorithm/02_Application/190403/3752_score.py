import sys
sys.stdin = open('3752.txt')

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    score = list(map(int, input().split()))
    result = set([0])

    for i in range(N):
        visit = set()
        for jj in result:
            visit.add(jj + score[i])
        result = result.union(visit)

    print('#{} {}'.format(test_case, len(result)))