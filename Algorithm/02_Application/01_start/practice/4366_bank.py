import sys
sys.stdin = open('4366.txt')

T = int(input())
for test_case in range(1, T + 1):
    two = input()
    three = input()
    two_list = []
    three_list = []

    for i in range(len(two)):
        Sum = 0
        for j in range(len(two)):
            if i == j:
                Sum += ((int(two[j]) + 1) % 2) * (2 ** (len(two) - j - 1))
            else:
                Sum += int(two[j]) * (2 ** (len(two) - j - 1))
        two_list += [Sum]

    list = []
    for i in range(len(three)):
        Sum = []
        n = 0
        for j in range(len(three)):
            if i == j:
                Sum_2 = []
                for k in range(3):
                    if k != int(three[j]):
                        Sum_2 += [k * (3 ** (len(three) - j - 1))]
                Sum += [Sum_2]
            else:
                n += int(three[j]) * (3 ** (len(three) - j - 1))
        Sum += [n]
        list += [Sum]
    for i in range(len(list)):
        for j in list[i][0]:
            three_list += [j + list[i][1]]

    print('#{}'.format(test_case),end=' ')
    for i in two_list:
        for j in three_list:
            if i == j:
                print(i)