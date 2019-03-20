import sys
sys.stdin = open('1970.txt')

T = int(input())
for test_case in range(1, T + 1):
    price = int(input())
    change = [0 for _ in range(8)]
    cash = [50000, 10000, 5000, 1000, 500, 100, 50, 10]

    for i in range(8):
        if price >= cash[i]:
            change[i] = price // cash[i]
            price = price % cash[i]

        if price == 0:
            break

    print('#{}'.format(test_case))
    for i in range(8):
        print(change[i], end=' ')
    print()
