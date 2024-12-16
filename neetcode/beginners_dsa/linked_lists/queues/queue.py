# regular queue, one way singly linked list implementation
# first implement node class
class Node:
    def __init__(self, value, next = None):
        self.val = value
        self.next = next
    
class Queue:
    def __init__(self):
        self.head = self.tail = None # not dummies

    def enqueue(self, value: int): # add to end
        new_node = Node(value)
        # check to see if tail exists
        if self.tail:
            self.tail.next = new_node
            self.tail = self.tail.next
        else:
            self.head = self.tail = new_node

    def dequeue(self): # remove first element and return
        if not self.head:
            return None
        
        value = self.head.val
        self.head = self.head.next
        if not self.head: # now list is empty check
            self.tail = None
        return value
