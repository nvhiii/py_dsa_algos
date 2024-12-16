class Node:
    def __init__(self, value):
        self.val = value
        self.prev = None
        self.next = None

class Deque:
    
    def __init__(self):
        self.head = Node(-1)
        self.tail = Node(-1) # dummies
        # lihnk
        self.head.next = self.tail
        self.tail.prev = self.head

    def isEmpty(self) -> bool:
        return self.head.next == self.tail

    def append(self, value: int) -> None:
        new_node = Node(value)
        # since adding to end, we find last actual node
        last_node = self.tail.prev
        last_node.next = new_node
        new_node.prev = last_node
        new_node.next = self.tail
        self.tail.prev = new_node

    def appendleft(self, value: int) -> None:
        new_node = Node(value)
        # since adding to front, we find first actual
        first_node = self.head.next
        self.head.next = new_node
        new_node.prev = self.head
        new_node.next = first_node
        first_node.prev = new_node

    def pop(self) -> int:
        if self.isEmpty():
            return -1
        last_node = self.tail.prev
        value = last_node.val # stored val
        next_last = last_node.prev

        next_last.next = self.tail
        self.tail.prev = next_last

        return value

    def popleft(self) -> int:
        if self.isEmpty():
            return -1
        # find first val node
        first_node = self.head.next
        # store val
        value = first_node.val
        next_first = first_node.next

        self.head.next = next_first
        next_first.prev = self.head

        return value
