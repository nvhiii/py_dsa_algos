class Node:
    def __init__(self, val, next):
        self.val = val
        self.next = next

class MyLinkedList:
    def __init__(self):
        self.head = Node(-1) # dummy
        self.tail = self.head # tail weont be dummy, only 1 dummy in this linked lsit

    def get(self, index):
        i = 0
        curr = self.head.next
        while curr:
            if i == index:
                return curr.val
            curr = curr.next
            i += 1
        return -1 # invalid index
    
    def addAtIndex(self, val):
        new_node = Node(val)
        new_node.next = self.head.next
        self.head.next = new_node
        if not new_node.next:
            self.tail = new_node

    def addAtTail(self, val):
        self.tail.next = Node(val)
        self.tail = self.tail.next

    def addAtIndex(self, index, val):
        i = 0
        curr = self.head # 0th indexing access
        while curr and i < index:
            curr = curr.next
            i += 1
        
        if curr: # since we add, no need to check index after
            new_node = Node(val)
            new_node.next = curr.next
            curr.next = new_node
            if not new_node.next:
                self.tail = new_node

    def deleteAtIndex(self, index):
        i = 0
        curr = self.head
        while curr and i < index:
            curr = curr.next
            i += 1

        if curr and curr.next: # here next val matters, since we are removing
            if curr.next == self.tail:
                self.tail = curr
            curr.next = curr.next.next
            return True
        return False