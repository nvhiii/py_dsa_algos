# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # dc
        if not lists or len(lists) == 0:
            return None
        
        # now split len of lists per iter
        while len(lists) > 1:
            merged_lists = [] # we merge 2 lists at a time
            for i in range(0, len(lists), 2): # steps of 2, for each list
                l1 = lists[i]
                l2 = lists[i + 1] if i + 1 < len(lists) else None # check for if lists init len is odd, we can still merge none
                merged_lists.append(self.merge(l1, l2)) # merge the lists, then append
            lists = merged_lists # reassign, and thus decrease len of lists itself logn, dividing by 2
        
        return lists[0] # return the merged list itself

    def merge(self, list1, list2):
        dummy = ListNode()
        tail = dummy # no need for a head in this sll

        while list1 and list2:
            if list1.val <= list2.val: # <= ensures a stable sort
                tail.next = list1 # next val after tail is newest val
                list1 = list1.next # iter to next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next # iterate the sll
        
        # if one of the lists havent been exhausted
        if list1:
            tail.next = list1
        if list2:
            tail.next = list2
        return dummy.next # return entire merged sll after iteration
