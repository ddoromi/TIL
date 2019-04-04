import sys
sys.stdin = open('1952.txt')

# T = int(input())
# for test_case in range(1, T + 1):
#     day_fee, month_fee, months_fee, year_fee = map(int, input().split())
#     plan = list(map(int, input().split()))
#     result = 0
#
#     for i in range(12):
#         plan[i] = min(plan[i] * day_fee, month_fee)
#
#     i = 0
#     while i < 12:
#         if plan[i] != 0:
#             fees = []
#             j = 0
#             while len(fees) < 5 and i + j < 12 and plan[i + j] != 0:
#                 fees.append(plan[i + j])
#                 j += 1
#             Min, index = 0xfffff, i
#             if len(fees) > 3:
#                 for k in range(len(fees) - 2):
#                     Sum = 0
#                     for l in range(k):
#                         Sum += fees[l]
#                     Sum += months_fee
#                     for l in range(k + 3, len(fees)):
#                         Sum += fees[l]
#                     if Min > Sum:
#                         Min, index = Sum, k
#                 i += index + 1
#                 result += Min
#             else:
#                 Min = min(sum(fees), months_fee)
#                 result += Min
#                 break
#         else:
#             i += 1
#     print(plan)
#     print(result)
#     for i in range(12):
#         result += plan[i]
#     print('#{} {}'.format(test_case, result))

T = int(input())
for test_case in range(1, T + 1):
    day, month, quarter, year = map(int, input().split())
    arr = list(map(int, input().split()))

    Min = year
    def dfs(k, cost):   # k: 월, cost: 지금까지 이용료
        global Min
        if cost >= Min:
            return
        if k >= 12:
            Min = min(Min, cost)
            return
        # 이용일이 있는 경우, 없는 경우
        if arr[k] == 0:
            dfs(k + 1, cost)
        else:
            dfs(k + 1, cost + arr[k] * day)
            dfs(k + 1, cost + month)
            dfs(k + 3, cost + quarter)
