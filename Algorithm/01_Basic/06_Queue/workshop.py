import sys
sys.stdin = open('workshop.txt')

T = int(input())
for test_case in range(T):
    P, Q, R, S, W = map(int, input().split())
    a_fee = W * P
    
    if W <= R:
        b_fee = Q
    else:
        b_fee = Q + (W - R) * S
    
    if a_fee > b_fee:
        result = b_fee
    else:
        result = a_fee
    
    print('#{} {}'.format(test_case + 1, result))
