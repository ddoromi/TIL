import sys
sys.stdin = open('5110.txt')


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class List:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_first(self, value):
        node = Node(value)
        if self.head is None:
            self.head = self.tail = node
        else:
            node.next = self.head
            self.head = node

    def insert_last(self, value):
        node = Node(value)
        if self.head is None:
            self.head = self.tail = node
        else:
            self.tail.next = node
            self.tail = node

    def insert_at(self, index, data):
        front, cur = None, self.head
        for i in range(index):
            front = cur
            cur = cur.next
        if front is None:
            self.insert_first(data[0])
            self.insert_at(1, data[1:])

        else:
            for i in range(len(data)):
                node = Node(data[i])
                node.next = cur
                front.next = node
                front = node
                cur = node.next


    def get_index(self, num):
        cur = self.head
        count = 0
        while cur is not None:
            if cur.value > num:
                return count
            else:
                count += 1
                cur = cur.next

    def print_list(self):
        cur = self.head
        result = []
        while cur is not None:
            result.append(cur.value)
            cur = cur.next
        return result

T = int(input())
for test_case in range(1, T+1):
    N, M = map(int, input().split())
    data = list(map(int, input().split()))
    sequence = List()
    Max = 0

    for i in range(M):
        sequence.insert_last(data[i])

    for i in range(M - 1):
        data = list(map(int, input().split()))
        index = sequence.get_index(data[0])
        if index == None:
            for j in range(M):
                sequence.insert_last(data[j])
        else:
            sequence.insert_at(index, data)

    print('#{}'.format(test_case), end=' ')
    result = sequence.print_list()
    for i in range(1, 11):
        print(result[-i], end=' ')
    print()
