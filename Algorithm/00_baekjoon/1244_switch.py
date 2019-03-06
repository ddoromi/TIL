import sys
sys.stdin = open('1244.txt')

switch_N = int(input())
switch = [0] + list(map(int, input().split()))
people_N = int(input())
people = []

for i in range(people_N):
    people.append(list(map(int, input().split())))

for i in range(0, people_N):
    j = people[i][1]

    if people[i][0] == 1:
        while j <= switch_N:
            switch[j] = (switch[j]+1) % 2
            j += people[i][1]
    else:
        k = 1
        switch[j] = (switch[j]+1) % 2
        while j-k >= 1 and j+k <= switch_N:
            if switch[j-k] == switch[j+k]:
                switch[j-k] = (switch[j-k]+1) % 2
                switch[j+k] = (switch[j+k]+1) % 2
                k += 1
            else:
                break

for i in range(1, switch_N+1):
    print(switch[i], end=' ')
    if i % 20 == 0:
        print()