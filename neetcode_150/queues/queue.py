class ListNode:
    def __init__(self, value, node = None):
        self.value = value
        self.next = node

class Queue:
    def __init__(self):
        self.head = None
        self.tail = self.head

    def enqueue(self, val):
        new_node = ListNode(val)
        if self.tail: # check not none
            self.tail.next = new_node
            self.tail = self.tail.next
        else:
            self.head = self.tail = new_node

    def dequeue(self): # remove 1st element
        if not self.head:
            return None
        
        val = self.head.value # store the val since we have to return it
        self.head = self.head.next
        if not self.head: # if removing element makes queue empty
            self.tail = None
        return val
