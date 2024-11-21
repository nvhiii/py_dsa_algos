# class ListNode:
#     def __init__(self, value, prev = None, next = None):
#         self.value = value
#         self.prev = prev
#         self.next = next

# class DoublyLinkedList:
#     def __init__(self):
#         self.head = ListNode(-1) # dummy
#         self.tail = self.head

#     # need to implement get, inserthead + tail, insertIth, deleteIth
#     def get(self, index): # same as the get method for singly linked list
#         i = 0 
#         curr = self.head.next
#         while curr:
#             if i == index:
#                 return curr.val
#             i += 1
#             curr = curr.next
#         return -1 # not found
    
#     def insertTail(self, val):
#         new_node = ListNode(val)
#         self.tail.next = new_node
#         new_node.prev = self.tail
#         self.tail = new_node

#     def insertHead(self, val):
#         new_node = ListNode(val)
#         new_node.next = self.head.next
#         self.head.next.prev = new_node
#         self.head = new_node

#     def insertIth(self, val, index):
#         i = 0
#         curr = self.head
#         while curr and i < index: # we iterate to node before
#             i += 1
#             curr = curr.next

#         if curr:
#             new_node = ListNode(val) # new node
#             new_node.next = curr.next # node points to next node after curr
#             curr.next.prev = new_node # changed node after prev pointer
#             new_node.prev = curr
#             curr.next = new_node
#             if not new_node.next:
#                 self.tail = new_node

    

