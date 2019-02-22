array = ['()()((()))', '((()((((()()((()())((())))))']
j = 0

for i in range(len(array)):
    checked = []
    while j < len(array[i]):
        if array[i][j] == '(':
            checked.append(array[i][j])
        else:
            if len(checked) == 0 or checked.pop(-1) != '(':
                print(False)
                break
        j += 1
        if j == len(array[i]):
            print(True)
