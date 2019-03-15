import sys
sys.stdin = open('3143.txt')

T = int(input())
for test_case in range(1 , T + 1):
    A, B = input().split()
    index = count =0

    while index < len(A):
        if (index <= len(A) - len(B)) and (A[index: index+len(B)] == B):
            index += len(B)
        else:
            index += 1
        count += 1
    print('#{} {}'.format(test_case, count))


    # for i in range(len(A) - len(B) + 1):
