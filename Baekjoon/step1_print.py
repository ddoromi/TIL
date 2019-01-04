#1. print('Hello World!')

# A , B = map(int, input().split())
# print(A - B)

# 2389. 배달하는 봉지의 최소 개수 출력

bag = int(input())

five, f_remainder = divmod(bag, 5)
three, t_remainder = divmod(f_remainder, 3)

if t_remainder == 0:
    print(five, three)
elif (f_remainder + 5) % 3 == 0:
    print(five-1, (t_remainder + 5)//3+1)
elif t_remainder % 3 == 0:
    print(five, three)
else:
    print(-1)

