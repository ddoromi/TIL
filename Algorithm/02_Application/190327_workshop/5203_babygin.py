import sys
sys.stdin = open('5203.txt')


def baby_gin(player):
    N = len(player)
    player.sort()
    count = 1
    for i in range(N - 1):
        if player[i] == player[i + 1]:
            count += 1
            if count >= 3:
                return 1
        else:
            count = 1
    count = 1
    for i in range(N - 1):
        if player[i + 1] - player[i] == 1:
            count += 1
            if count >= 3:
                return 1
        elif player[i + 1] - player[i] > 1:
            count = 1

T = int(input())
for test_case in range(1, T + 1):
    nums = [0] + list(map(int, input().split()))
    player1, player2 = [], []
    for i in range(1, 13):
        if i % 2:
            player1.append(nums[i])
            if len(player1) >= 3 and baby_gin(player1):
                result = 1
                break
        else:
            player2.append(nums[i])
            if len(player2) >= 3 and baby_gin(player2):
                result = 2
                break
    else:
        result = 0
    print('#{} {}'.format(test_case, result))