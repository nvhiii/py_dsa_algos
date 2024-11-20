class ListNode:
    def __init__(self, value, prev = None, next = None):
        self.value = value
        self.prev = prev
        self.next = next

class DoublyLinkedList:
    def __init__(self):
        self.head = ListNode(-1) # dummy
        self.tail = self.head

# access, inserthead + inserttail, insertith, deleteith
    