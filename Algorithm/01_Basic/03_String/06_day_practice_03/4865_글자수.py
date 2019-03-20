import sys
sys.stdin = open('4865.txt')

T = int(input())

for t in range(T):
    result = {}
    text = input()
    pattern = input()
    Max = 0

    for i in range(len(text)):
        result[text[i]] = 0

    for i in range(len(pattern)):
        for char in result:
            count = 0
            if char == pattern[i]:
                result[char] += 1
    
    for char in result:
        if result[char] > Max:
            Max = result[char]
    
    print(f'#{t+1} {Max}')
        
        