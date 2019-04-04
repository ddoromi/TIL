import sys
sys.stdin = open('4111.txt')

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    K = int(input())
    camera = list(map(int, input().split()))
    camera.sort()
    distance = []
    for i in range(1, N):
        distance.append(camera[i] - camera[i - 1])
    distance.sort()
    Sum = 0
    for i in range(0, len(distance) - (K - 1)):
        Sum += distance[i]
    print('#{} {}'.format(test_case, Sum))
