# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# generalization: lots of ll uses two pointer method

class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        prev, curr = None, head # 2 pointer method
        while curr:
            temp = curr.next
            curr.next = prev # reverse the pointer direction
            prev = curr # go to next
            curr = temp
        return prev