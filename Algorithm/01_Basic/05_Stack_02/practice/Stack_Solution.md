# Stack_Solution

### 4881_ 배열 최소 합

```python
import sys
sys.stdin = open("5286.txt", "r")

MIN = 0
def perm(k, n, used, cursum):  # used: 더한 요소, cursum: 부분집합의 합
    global MIN
    if cursum >= MIN:
        return
    if k == n:
        if cursum < MIN:
            MIN = cursum
        return

    for i in range(n):  # 어떤 원소를 골랐는지 저장할 필요는 없음
        if used & (1 << i):  continue
        perm(k + 1, n, used | (1 << i), cursum + arr[k][i])  # k행 i열


T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    arr = []
    for i in range(N):
        arr.append(list(map(int, input().split())))

    MIN = 0xffffff  # 가장 큰 값으로 초기화함
    perm(0, N, 0, 0)  # 0부터 N까지

    print("#%d %d" % (test_case, MIN))
```

### 4880_토너먼트

```python
import sys
sys.stdin = open("5286.txt", "r")


win = {1: 3, 2: 1, 3: 2}


def play(lo, hi):
    if lo == hi:
        return lo

    mid = int((lo + hi)/2)

    l = play(lo, mid)
    r = play(mid + 1, hi)

    if cards[l] == cards[r] or win[cards[l]] == cards[r]:
        return l

    return r


T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    cards = list(map(int, input().split()))

    print("#%d %d" % (test_case, play(0, len(cards) - 1) + 1))
    
```

### 1224_계산기3

```python
import sys
sys.stdin = open("5286.txt", "r")

icp = {'+': 1, '-': 1, '*': 2, '/': 2, '(': 3}
isp = {'+': 1, '-': 1, '*': 2, '/': 2, '(': 0}

for test_case in range(1, 11):
    N = int(input())
    infix = input()
    postfix = ''

    S = []

    for ch in infix:
        if ch == ')':
            while S[-1] != '(':
                postfix += S.pop()
            S.pop()
        elif ch in icp:
            if len(S) == 0:
                S.append(ch)
                continue

            while len(S) and isp[S[-1]] >= icp[ch]:
                postfix += S.pop()
            S.append(ch)
        else:
            postfix += ch

    while len(S) > 0:
        postfix += S.pop()


    S = []
    for ch in postfix:
        if ch in isp:
            b, a = S.pop(), S.pop()
            if ch == '+':
                S.append(a + b)
            elif ch == '-':
                S.append(a - b)
            elif ch == '*':
                S.append(a * b)
            else:
                S.append(a // b)
        else:
            S.append(int(ch))

    print("#%d %d" % (test_case, S[0]))
```

### 4875_미로

```python
import sys
sys.stdin = open("4875.txt", "r")


sx = sy = ex = ey = 0
diff = [(0, 1), (0, -1), (1, 0), (-1, 0)]


def DFS(x, y):
    visit[x][y] = True  # 방문표시

    for (dx, dy) in diff:
        tx, ty = x + dx, y + dy
        if tx < 0 or tx == N or ty < 0 or ty == N:  # 경계확인
            continue
        if visit[tx][ty] or maze[tx][ty] == '1':
            continue

        DFS(tx, ty)

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())

    maze = []
    visit = [[False for i in range(N)] for j in range(N)]

    for i in range(N):
        maze.append(input())
        for j in range(N):
            if maze[i][j] == '2':
                sx, sy = i, j
            if maze[i][j] == '3':
                ex, ey = i, j

    DFS(sx, sy)
    print("#%d %d" % (test_case, visit[ex][ey]))
```





