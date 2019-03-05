N, K = map(int, input().split())
wheel = [0] * N
array = []
start = 0
result = ''

for i in range(K):
    a, b = input().split()
    array.append([int(a), b])

for i in range(K):
    index = (start - array[i][0]) % N
    if (wheel[index] == 0) or (wheel[index] == array[i][1]):
        wheel[index] = array[i][1]
        start = index
    else:
        result = '!'
        break

else:
    for i in range(N):
        if wheel[i] == 0:
            wheel[i] = '?'
        else:
            if wheel[i] in result:
                result = '!'
                break
        result += wheel[i]

    else:
        result = wheel[wheel.index(array[-1][1]):N] + wheel[0:wheel.index(array[-1][1])]

print(''.join(result))




