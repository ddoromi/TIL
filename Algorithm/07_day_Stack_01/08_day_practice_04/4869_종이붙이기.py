import sys
sys.stdin = open('4869.txt')


def stick(N, result):
    global count
    if N <= 10:
        count += result
        return count
    else:
        for p in paper.keys():
            stick(N - p, result * paper[p])


T = int(input())
paper = {10: 1, 20: 2}

for t in range(T):
    N = int(input())
    count = 0
    stick(N, 1)
    print(f'#{t+1} {count}')



