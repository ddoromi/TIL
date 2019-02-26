Sum, result = 0, 0
Min = 100

for i in range(10):
    mushroom = int(input())
    Sum += mushroom
    if abs(100-Sum) <= Min:
        Min = abs(100-Sum)
        result = max(result, Sum)

print(result)
