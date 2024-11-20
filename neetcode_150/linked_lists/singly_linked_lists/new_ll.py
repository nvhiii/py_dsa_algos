# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)

class ListNode:
    def __init__(self, value, node = None):
        self.value = value
        self.next = node
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
        i = 0
        curr = self.head
        while curr and i < index:
            i += 1
            curr = curr.next

        if curr and curr.next:
            if curr.next == self.tail:
                self.tail = curr
            curr.next = curr.next.next
            return True
        return False