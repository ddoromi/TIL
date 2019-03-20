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


    def printlist(self):
        if self.head is None:      # 빈 리스트 처리가 필요함
            print('빈 리스트입니다.')
        else:
            print(self.size, '[ ', end='')
            cur = self.head
            while cur is not None:
                print(cur.data, end=' ')
                cur = cur.next
            print(']')


    def insertlast(self, val):
        node = Node(val)
        if self.head is None:      # 빈 리스트 처리가 필요함
            self.head = self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        self.size += 1


    def insertfirst(self, val):
        node = Node(val)
        if self.head is None:
            self.head = self.tail = node
        else:
            node.next = self.head
            self.head = node
        self.size += 1


    def deletelast(self):
        if self.head is None:
            print('빈 리스트 입니다.')
        else:
            prev, cur = None, self.head
            while cur.next is not None:
                prev = cur
                cur = cur.next
        if prev is None:
            self.head = self.tail = None
            del cur
        else:
            prev.next = None
            self.tail = prev
            del cur


    def deletefirst(self):
        if self.head is None:
            print('빈 리스트 입니다.')
        else:
            cur = self.head
            if cur.next is None:
                self.head = self.tail = None
            else:
                self.head = cur.next
            del cur
            self.size -= 1

    def insertAt(self, idx, val):
        if self.head is None:
            self.insertfirst(val)
        elif idx >= self.size:
            self.insertlast(val)
        else:
            prev, cur = None, self.head
            for i in range(idx):
                prev = cur
                cur = cur.next
            if prev is None:
                self.insertfirst(val)
            else:
                node = Node(val)
                node.next = prev.next
                prev.next = node
        self.size += 1


    def deleteAt(self, idx):
        if self.head is None:
            self.deletefirst()
        elif idx >= self.size:
            print('잘못된 인덱스입니다.')
        else:
            prev, cur = None, self.head
            for i in range(idx):
                prev = cur
                cur = prev.next
            if prev is None:
                self.deletefirst()
            else:
                prev.next = cur.next
                del cur

mylist = List()
mylist.insertfirst(1)
mylist.insertfirst(2)
mylist.insertfirst(3)
mylist.insertfirst(4)
mylist.insertfirst(5)
mylist.printlist()
mylist.deleteAt(4)
mylist.printlist()