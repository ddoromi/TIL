import sys
sys.stdin = open('input.txt')
sys.stdout = open('output.txt', 'w')
T = int(input())

for t in range(T):
    case, N = input().split()
    nums = list(map(str, input().split()))
    num_dict = ['ZRO', 'ONE', 'TWO', 'THR', 'FOR', 'FIV', 'SIX', 'SVN', 'EGT', 'NIN']
    count = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    for i in range(len(nums)):
        for j in range(len(num_dict)):
            if num_dict[j] == nums[i]:
                count[j] += 1
    
    print(f'{case}')
    for i in range(len(num_dict)):
        for j in range(count[i]):
            print(f'{num_dict[i]}', end=' ')