# reverse a linked list using recursion

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr, prev = head, None
        while curr:
            temp = curr.next # store this pointer, or we will lose the next val
            curr.next = prev # swapped dir of pointer!
            prev = curr # prev pointer moves to the right
            curr = temp # curr pointer moves to the right
            # therefore, eventually curr = None, so have to return prev
        
        return prev