import sys
sys.stdin = open('1244.txt')

T = int(input())
for test_case in range(1, T + 1):
    board, N = input().split()
    board, N = list(board), int(N)
    for b in range(len(board)):
        board[b] = int(board[b])
    board2 = sorted(board, reverse=True)

    j, i = 0, 0
    while i < N:
        Max, index = board[j], j
        for k in range(j + 1, len(board)):
            if board[k] >= Max:
                Max, index = board[k], k
        if j != index:
            board[j], board[index] = board[index], board[j]
            if board[0] == board[1]:
                if index < len(board) - 1 and board[index + 1] > board[index]:
                    board[index + 1], board[index] = board[index], board[index + 1]
            j, i = j + 1, i + 1
        else:
            j += 1
        if board == board2:
            break

    if (N - i) % 2:
        board[-1], board[-2] = board[-2], board[-1]
    print('#{}'.format(test_case), end=' ')
    for ii in board:
        print(ii, end='')
    print()


# 깊이 우선
def find_max(k, n):     # k: 현재 교환 횟수, n: 교환 해야 할 횟수
    global MAX
    val = int(''.join(map(str, arr)))
    if k == n:
        if val > MAX:
            MAX = val
            print(MAX)
        return
    if val in visit[k]: return
    visit[k].append(val)

    for i in range(N - 1):
        for j in range(i + 1, N):
            arr[i], arr[j] = arr[j], arr[i]
            find_max(k + 1, n)
            arr[i], arr[j] = arr[j], arr[i]

arr = [4, 5, 6, 7, 8, 9]
N = len(arr)
visit = [[] for _ in range(11)]
MAX = 0
find_max(0, 10)
print(MAX)
