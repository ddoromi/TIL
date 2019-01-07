numbers = [1, 2, 3] # 변수 이름은 뜻을 담아서 짓자!
family = ['mom', 1.64, 'dad', 1.75, 'sister', 1.78, 'mom', 1.64, 'dad', 1.75, 'sister', 1.78]
family[-1]

mcu = [
    ['ironman', 'captain america', 'dr.strange'], 
    ['xmen', 'deadpool'],
    ['spiderman']
]
disney = mcu[0]
disney[2]
mcu[0][2]

['this', 'hits', 1, True, "List"]
['this', 12, ['a', 'c', 'c'], False]
['I', "am", "iron", "man", "True"]
[
    "Iron" + "man",
    "spider" + True,
    1 + 2
]
['a', 'b', 'c', 'c']

numbers = list(range(1, 46))
numbers[1: 10]
numbers[2: 5] # [start:end] => start 는 포함, end 안 포함!

x = ['x', 'y', 'z', True, 123, ['a', 'b', 'c']]
my_bool = x[3]
my_bool = x[-3]