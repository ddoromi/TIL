my_number = set([1, 23, 8, 41, 36, 45])
real_number = set([1, 11, 23, 36, 41, 45])
bonus_number = 8

if my_number == real_number :
    print('1등 입니다. 예~~~~~~~~~~~~~~~~~~~')
else :
    if len(real_number & my_number) == 4 :
        print('3등 입니다. 예~~~~~~~~~~~~~~~~~~~')
    elif len(real_number & my_number) == 3 :
        print('4등 입니다. 예~~~~~~~~~~~~~~~~~~~')
    else :
        real_number.add(bonus_number)
        print(real_number)
        if len(real_number & my_number) == 6 :
            print('2등 입니다. 예~~~~~~~~~~~~~~~~~~~')
        else :
            print('꽝 입니다. 예~~~~~~~~~~~~~~~~~~~')

