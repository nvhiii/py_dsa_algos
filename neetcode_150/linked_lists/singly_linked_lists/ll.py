# Design a Singly Linked List class.

# Your LinkedList class should support the following operations:

# LinkedList() will initialize an empty linked list.
# int get(int i) will return the value of the ith node (0-indexed). If the index is out of bounds, return -1.
# void insertHead(int val) will insert a node with val at the head of the list.
# void insertTail(int val) will insert a node with val at the tail of the list.
# bool remove(int i) will remove the ith node (0-indexed). If the index is out of bounds, return false, otherwise return true.
# int[] getValues() return an array of all the values in the linked list, ordered from head to tail.

class ListNode:
    def __init__(self, value, node = None):
        self.value = value
        self.next = node

class LinkedList:
    def __init__(self):
        self.head = ListNode(-1)
        self.tail = self.head

    # get
    def get(self, i):
        index = 0
        curr = self.head.next # first non dummy val
        while curr:
            if index == i:
                return curr.val
            index += 1
            curr = curr.next
        return -1 # not found
    
    # insert head
    def insertHead(self, val):
        new_node = ListNode(val)
        new_node.next = self.head.next
        self.head.next = new_node
        if not new_node.next:
            self.tail = new_node

    # insert tail
    def insertTail(self, val):
        self.tail.next = ListNode(val)
        self.tail = self.tail.next

    # remove
    def remove(self, i): # index
        curr = self.head
        index = 0
        while curr and index < i:
            index += 1
            curr = curr.next # iterate until node before

        if curr and curr.next:
            if curr.next == self.tail:
                self.tail = curr
            curr.next = curr.next.next
            return True
        return False
    
    def getValues(self):
        res = []
        curr = self.head.next
        while curr:
            res.append(curr.val)
            curr = curr.next
        return res