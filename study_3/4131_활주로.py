import sys
sys.stdin = open('4131.txt')

T = int(input())
for test_case in range(1, T + 1):
    MAP = []
    N, X = map(int, input().split())
    airstrip = 0
    for i in range(N):
        MAP.append(list(map(int, input().split())))

    # 각 행에 대해 최고 높이를 찾고 스택을 초기화함.
    for i in range(N):
        max_height = max(MAP[i])
        stack = []
        check = True
        check_2 = True
        for j in range(N):
            if MAP[i][j] == max_height and len(stack) > 0 and check_2 == False:
                check = False
                break
            if MAP[i][j] == max_height and len(stack) == 0:
                check = False
                continue
            if MAP[i][j] != max_height:
                stack.append(MAP[i][j])
            else:
                if len(stack) < X or stack[-1] != max_height - 1:
                    check = False
                    break
                else:
                    count = 1
                    for k in range(1, len(stack)):
                        if stack[-k] == stack[-k - 1]:
                            count += 1
                        else:
                            if count < X or stack[-k] != stack[-k-1] - 1:
                                check = False
                                break
                            else:
                                count = 1
                    if check == False:
                        break
                    else:
                        check = True
                        stack = []
        else:
            if len(stack) == 0:
                check = True
            elif len(stack) < X or stack[0] != max_height - 1:
                continue
            else:
                count = 1
                for k in range(len(stack) - 1):
                    if stack[k] == stack[k + 1]:
                        count += 1
                    else:
                        if count < X:
                            break
                        else:
                            count = 1
                if count < X:
                    check = False
                else:
                    check = True
        if check:
            airstrip += 1
            print(i, airstrip)

    for i in range(N):
        max_height = 0
        for k in range(N):
            if max_height < MAP[k][i]:
                max_height = MAP[k][i]
        stack = []
        check = True
        check_2 = True
        for j in range(N):
            if MAP[j][i] == max_height and len(stack) > 0 and check_2 == False:
                check = False
                break
            if MAP[j][i] == max_height and len(stack) == 0:
                check = False
                continue
            if MAP[j][i] != max_height:
                stack.append(MAP[j][i])
            else:
                if len(stack) < X or stack[-1] != max_height - 1:
                    check = False
                    break
                else:
                    count = 1
                    for k in range(1, len(stack)):
                        if stack[-k] == stack[-k - 1]:
                            count += 1
                        else:
                            if count < X:
                                check = False
                                break
                            else:
                                count = 1
                    if check == False:
                        break
                    else:
                        check = True
                        stack = []
        else:
            if len(stack) == 0:
                check = True
            elif len(stack) < X or stack[0] != max_height - 1:
                continue
            else:
                count = 1
                for k in range(len(stack) - 1):
                    if stack[k] == stack[k + 1]:
                        count += 1
                    else:
                        if count < X:
                            break
                        else:
                            count = 1
                if count < X:
                    check = False
                else:
                    check = True
        if check:
            airstrip += 1
    print('#{} {}'.format(test_case, airstrip))