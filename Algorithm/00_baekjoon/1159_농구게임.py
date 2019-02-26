players = int(input())
name = {}
result = []

for p in range(players):
    player = input()
    if player[0] not in name:
        name[player[0]] = 1
    else:
        name[player[0]] += 1
        if name[player[0]] == 5:
            result.append(player[0])

j = 0
while j < len(result):
    Min = result[j]
    idx = j
    for i in range(j+1, len(result)):
        if Min > result[i]:
            Min = result[i]
            idx = i
    result[j], result[idx] = result[idx], result[j]
    j += 1

if len(result) == 0:
    print('PREDAJA')
else:
    print(''.join(result))
