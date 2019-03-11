class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __del__(self):
        print(self.data, '삭제')

class List:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def deletefirst(self):
        if self.head is None:
            print('빈 리스트입니다.')
        else:
            cur = self.head
            if cur.next is None:
                self.head = self.tail = None
            self.head = cur.next
            del cur
        self.size -= 1