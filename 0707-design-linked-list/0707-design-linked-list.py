class Node:
    def __init__(self, val = 0):
        self.val = val
        self.next = None
class MyLinkedList:

    def __init__(self):
        self.head = None
        self.size = 0

    def get(self, index: int) -> int:
        if index >= self.size or index < 0:
            return -1
        else:
            cnt = 0
            cur = self.head
            while cnt < index:
                cur = cur.next
                cnt = cnt + 1
            if cur != None:
                return cur.val
            else:
                return -1
        

    def addAtHead(self, val: int) -> None:
        node = Node(val)
        node.next = self.head
        self.head = node
        self.size = self.size + 1
        

    def addAtTail(self, val: int) -> None:
        if self.size == 0:
            self.addAtHead(val)
        else:
            node = Node(val)
            cnt = 0
            cur = self.head
            index = self.size - 1
            while cnt < index:
                cur = cur.next
                cnt = cnt + 1
            cur.next = node
            self.size = self.size + 1
        

    def addAtIndex(self, index: int, val: int) -> None:
        if index == 0:
            self.addAtHead(val)
        elif index == self.size:
            self.addAtTail(val)
        elif 0 < index and index < self.size:
            node = Node(val)
            cnt = 0
            cur = self.head
            index = index - 1
            while cnt < index:
                cur = cur.next
                cnt = cnt + 1
            node.next = cur.next
            cur.next = node
            self.size = self.size + 1
        else:
            return
        

    def deleteAtIndex(self, index: int) -> None:
        if index == 0:
            self.head = self.head.next
            self.size = self.size - 1
        elif 0 < index and index < self.size:
            cnt = 0
            cur = self.head
            index = index - 1
            while cnt < index:
                cur = cur.next
                cnt = cnt + 1
            cur.next = cur.next.next
            self.size = self.size - 1
        else:
            return
            
        


