import sys
sys.stdin = open('4836.txt')

T = int(input())
for t in range(T):

    arr = []
    for c in range(10):
        arr.append([0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
    data = []
    count = 0
    N = int(input())

    for n in range(N):
        data.append(list(map(int, input().split())))

    for n in range(N):
        for i in range(data[n][0], data[n][2]+1):
            for j in range(data[n][1], data[n][3]+1):
                if arr[i][j] != 0 and arr[i][j] != data[n][4]:
                    count += 1
                else:
                    arr[i][j] = data[n][4]

    print(f"#{t+1} {count}")
