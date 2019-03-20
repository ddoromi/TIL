# # 이진수 => 10진수
# data = ['0000000111100000011000000111100110000110000111100111100111111001100111']
# result = []
#
# data = list(data[0])
# for i in range(0, len(data), 7):
#     Sum = 0
#     for j in range(7):
#         Sum += int(data[i+j]) * (2 ** (6 - j))
#     result.append(Sum)
# print(result)

# 16진수 => 10진수
data = '01D06079861D79F99F'
data = list(data)
result = []
array = []
dictionary = {'A' :'1010', 'B': '1011', 'C': '1100', 'D': '1101', 'E': '1110', 'F': '1111'}
for i in range(len(data)):
    if data[i] in dictionary:
        array += list(dictionary[data[i]])
    else:
        temp = str(format(int(data[i]), 'b'))
        array += list('0' * (4 - len(temp)) + temp)
for i in range(0, len(array) - 2, 7):
    Sum = 0
    for j in range(7):
        Sum += int(array[i+j]) * (2 ** (6 - j))
    result.append(Sum)
print(result)

# import sys
#
# d = [20, 1, 30, 10, 10]
# M = [[0 for x in range(5)] for y in range(5)]
# for diag in range(1, 5):
#     for i in range(1, 5 - diag):
#         j = i + diag
#         M[i][j] = sys.maxsize
#         for k in range(i, j):
#             M[i][j] = min(M[i][j],
#                           M[i][k] + M[k + 1][j] + d[i - 1] * d[k] * d[j])
#
# print(M[1][4])