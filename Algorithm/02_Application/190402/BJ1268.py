import sys
sys.stdin = open('BJ1268.txt')

N = int(input())
student = []
for i in range(N):
    student.append(list(map(int, input().split())))
count = [[i] for i in range(N)]

for i in range(N):
    for j in range(5):
        for l in range(N):
            if (student[i][j] == student[l][j]) and (l not in count[i]):
                count[i] += [l]
for i in range(N):
    count[i] = len(count[i]) - 1
Max = 0
index = 0
for i in range(N):
    if count[i] > Max:
        Max, index = count[i], i
print(index + 1)

