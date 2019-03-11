import sys
sys.stdin = open('5120.txt')


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __del__(self):
        print(self.data, '삭제')


class List:
    def __init__(self):
        self.head = None  # 첫번째 노드 참조
        self.tail = None
        self.size = 0

    def insert_first(self, val):
        node = Node(val)
        if self.head is None:
            self.head = self.tail = node
        else:
            node.next = self.head
            self.head = node
        self.size += 1

    def insert_last(self, val):
        node = Node(val)
        if self.head is None:      # 빈 리스트 처리가 필요함
            self.head = self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        self.size += 1

    def insert_at(self, idx, val):
        prev, cur = None, self.head
        for i in range(idx):
            prev = cur
            cur = cur.next
        if prev is None:
            self.insert_first(val)
        else:
            node = Node(val)
            node.next = prev.next
            prev.next = node
        self.size += 1


T = int(input())
for test_case in range(1, T+1):
    N, M, K = map(int, input().split())
    sequence = list(map(int, input().split()))
    index, count = M, 1
    my_list = List()

    for i in range(N):
        my_list.insert_last(sequence[i])

    while count <= K:
        val = sequence[index-1] + sequence[index]
        sequence.insert(index, val)
        index = (index + M) % len(sequence)
        count += 1

    print(sequence)


