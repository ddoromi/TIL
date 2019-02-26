arr = [1, 2, 3, 5, 6, 7, 8, 9, 10]

n = len(arr)

for i in range(1 << n): # 0 ~ 63
    result = 0

    # 2^0 ~ 2^5에 해당하는 비트 값을 확인
    for j in range(n):
        if i & (1 << j) != 0:
            result += arr[j]
            # print(arr[j], end='')

    if result == 10:
        for j in range(n):
            if i & (1 << j) != 0:
                print(arr[j], end='')
        print()


# for i in range(1<<n):
#     for j in range(n+1):
#         if i & (i<<j):
#             print(arr[j], end='')
#     print()
# print()
