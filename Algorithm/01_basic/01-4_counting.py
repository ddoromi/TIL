k = 4
arr = [0, 4, 1, 3, 1, 2, 4, 1]
cnt = [0] * (k+1)
sorted = [0] * len(arr)
for val in arr:
    cnt[val] += 1

print(cnt)

#cnt를 이용하여 arr을 카운팅 배열
# index = 0
# for i in range(k+1):
#     for j in range(cnt[i]):
#         arr[index] = i
#         index += 1

# print(arr)


for i in range(1, k+1):
    cnt[i] = cnt[i-1] + cnt[i]

print(cnt)


for val in range(len(arr)-1, -1, 0):
    cnt[arr[i]] -= 1
    sorted[cnt[arr[]]]
