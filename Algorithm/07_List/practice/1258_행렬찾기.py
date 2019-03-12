import sys
sys.stdin = open('1258.txt')

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    matrix = []
    sub_matrix = []

    for i in range(N):
        matrix.append(list(map(int, input().split())))

    for i in range(N):
        for j in range(N):
            if matrix[i][j] > 0:
                x_count, x_index = 0, i
                y_count, y_index = 0, j

                while matrix[i][y_index]:
                    y_index += 1
                    y_count += 1

                for k in range(i, N):
                    if matrix[k][j] == 0:
                        break
                    else:
                        x_count += 1
                    for l in range(y_count):
                        matrix[k][j+l] = 0

                sub_matrix.append([x_count, y_count])

    for i in range(len(sub_matrix)):
        Min = sub_matrix[i][0] * sub_matrix[i][1]
        index = i
        for j in range(i + 1, len(sub_matrix)):
            if Min > (sub_matrix[j][0] * sub_matrix[j][1]):
                Min = sub_matrix[j][0] * sub_matrix[j][1]
                index = j
        sub_matrix[i], sub_matrix[index] = sub_matrix[index], sub_matrix[i]

    print('#{} {}'.format(test_case, len(sub_matrix)), end=' ')
    for i in range(len(sub_matrix)):
        print(sub_matrix[i][0], sub_matrix[i][1], end=' ')
    print()