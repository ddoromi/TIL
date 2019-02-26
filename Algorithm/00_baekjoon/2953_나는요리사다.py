data = []
Max = 0

for i in range(5):
    data.append(list(map(int, input().split())))

for i in range(5):
    Sum = 0
    for j in range(4):
        Sum += data[i][j]
    if Sum > Max:
        Max = Sum
        player = i+1

print(f'{player} {Max}')
