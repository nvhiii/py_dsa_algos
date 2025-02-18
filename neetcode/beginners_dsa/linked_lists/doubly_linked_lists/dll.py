# this is node class
class Node:
    def __init__(self, val, prev, next):
        self.val = val
        self.prev = None
        self.next = None

# linked list implementation
class DLL:
    def __init__(self):
        self.head = Node(-1)
        self.tail = Node(-1)

        # linked the dummy nodes, easier access
        self.head.next = self.tail
        self.tail.prev = self.head

    def insertFront(self, val):
        # insert after the dummy head
        nn = self.head.next
        new_node = Node(val)

        # to be safe, may need to add a check for empty list aside the dummy nodes
        self.head.next = new_node
        new_node.prev = self.head
        new_node.next = nn
        nn.prev = new_node

    def insertEnd(self, val):
        pn = self.tail.prev
        
        new_node = Node(val)
        pn.next = new_node
        new_node.prev = pn
        new_node.next = self.tail
        self.tail.prev = new_node

    def removeFront(self):
        # so we remove first node after dummy head
        if self.head != self.tail:
            removed = self.head.next
            new_next = removed.next
            
            self.head.next = new_next
            new_next.prev = self.head


    def removeEnd(self):
        if self.head != self.tail:
            removed = self.tail.prev
            new_prev = removed.prev

            new_prev.next = self.tail
            self.tail.prev = new_prev

    