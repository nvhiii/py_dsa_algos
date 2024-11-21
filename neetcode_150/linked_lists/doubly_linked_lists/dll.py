class Node:
    def __init__(self, value):
        self.val = value
        self.prev = None
        self.next = None


class MyLinkedList(object):

    def __init__(self):
        self.head = Node(-1)
        self.tail = Node(-1) # dummies
        # link them
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, index):
        """
        :type index: int
        :rtype: int
        """
        curr = self.head.next # first non dummy
        while curr and index > 0:
            curr = curr.next
            index -= 1
        if curr and curr != self.tail and index == 0:
            return curr.val
        return -1 # not found
        

    def addAtHead(self, val):
        """
        :type val: int
        :rtype: None
        """
        first = self.head
        node = Node(val)
        second = self.head.next

        first.next = node
        node.prev = first
        node.next = second
        second.prev = node

    def addAtTail(self, val):
        """
        :type val: int
        :rtype: None
        """
        first = self.tail.prev
        node = Node(val)
        second = self.tail

        first.next = node
        node.prev = first
        node.next = second
        second.prev = node

    def addAtIndex(self, index, val):
        """
        :type index: int
        :type val: int
        :rtype: None
        """
        curr = self.head.next # first non dummy to iter
        while curr and index > 0:
            curr = curr.next
            index -= 1
        if curr and index == 0:
            # we iterated to exact index to add at
            first = curr.prev
            node = Node(val)

            first.next = node
            node.prev = first
            node.next = curr
            curr.prev = node

    def deleteAtIndex(self, index):
        """
        :type index: int
        :rtype: None
        """
        curr = self.head.next
        while curr and index > 0:
            curr = curr.next
            index -= 1
        if curr and curr != self.tail and index == 0:
            # curr is the target index
            first = curr.prev
            skip_to = curr.next

            first.next = skip_to
            skip_to.prev = first
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)