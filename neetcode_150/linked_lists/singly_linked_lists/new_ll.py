<<<<<<< HEAD
=======
# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)

>>>>>>> 175ee6e485718842fd2af75c94dc01f69263ea49
class ListNode:
    def __init__(self, value, node = None):
        self.value = value
        self.next = node
<<<<<<< HEAD

class MyLinkedList(object):

    def __init__(self):
        self.head = ListNode(-1) # dummy for getting
        self.tail = self.head

    def get(self, index):
        """
        :type index: int
        :rtype: int
        """
        i = 0
        curr = self.head.next # skip first idx
        while curr:
            if i == index:
                return curr.value
            i += 1
            curr = curr.next
        return -1
        

    def addAtHead(self, val):
        """
        :type val: int
        :rtype: None
        """
        new_node = ListNode(val)
        new_node.next = self.head.next
        self.head.next = new_node
        if not new_node.next:
            self.tail = new_node

    def addAtTail(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.tail.next = ListNode(val)
        self.tail = self.tail.next
        

    def addAtIndex(self, index, val):
        """
        :type index: int
        :type val: int
        :rtype: None
        """
        i = 0
        curr = self.head
        while curr and i < index:
            i += 1
            curr = curr.next # get up to node before the indexed node

        if curr: # curr is not None
            new_node = ListNode(val)
            new_node.next = curr.next
            curr.next = new_node
            if not new_node.next:
                self.tail = new_node
    
    def deleteAtIndex(self, index):
        """
        :type index: int
        :rtype: None
        """
=======
        # no prev in singly linked lists

class SinglyLinkedList:
    def __init__(self):
        self.head = ListNode(-1) # dummy
        self.tail = self.head

    # get o(1), insertHead + tail o(1), insertith o(n), deleteith o(n)
    def get(self, index): # return val of node at index specified
        i = 0
        curr = self.head.next # skip the dummy
        while curr:
            if i == index:
                return curr.value # value bc of the listnode instance vars
            i += 1 # iterate to next idx
            curr = curr.next # make the node the next node the curr node points to
        # not found
        return -1
    
    def insertHead(self, val):
        new_node = ListNode(val)
        new_node.next = self.head.next # skip dummy
        self.head.next = new_node # head is always dummy
        if not new_node.next:
            self.tail = new_node

    def insertTail(self, val):
        self.tail.next = ListNode(val)
        self.tail = self.tail.next

    def insertIth(self, val, index):
        i = 0
        curr = self.head # must iterate using 0th indexing
        while curr and i < index: # iterate to prev node
            i += 1
            curr = curr.next
        if curr:
            new_node = ListNode(val)
            new_node.next = curr.next
            curr.next = new_node
            if not new_node.next: # if new new node is last
                self.tail = new_node

    def deleteIth(self, index):
>>>>>>> 175ee6e485718842fd2af75c94dc01f69263ea49
        i = 0
        curr = self.head
        while curr and i < index:
            i += 1
            curr = curr.next

<<<<<<< HEAD
        if curr and curr.next: # both must be valid
            if curr.next == self.tail:
                self.tail = curr
            curr.next = curr.next.next # removes the pointer to direct next node
            return True
        return False


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
=======
        if curr and curr.next:
            if curr.next == self.tail:
                self.tail = curr
            curr.next = curr.next.next
            return True
        return False
>>>>>>> 175ee6e485718842fd2af75c94dc01f69263ea49
