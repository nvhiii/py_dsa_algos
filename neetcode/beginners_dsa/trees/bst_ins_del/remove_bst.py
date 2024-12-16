# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):

    # helper for in successor order
    def findMinNode(self, root):
        curr = root
        while curr and curr.left:
            curr = curr.left
        return curr

    def deleteNode(self, root, key):
        """
        :type root: Optional[TreeNode]
        :type key: int
        :rtype: Optional[TreeNode]
        """
        # no tree case
        if not root:
            return None
        
        # iter to key node
        if key > root.val:
            root.right = self.deleteNode(root.right, key)
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        else: # got to key node
        # handle node if only one child or less first
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            else: # 2 children case
                # in successor order
                min_node_greater = self.findMinNode(root.right) # we want to fight next smallest but greater node
                root.val = min_node_greater.val
                root.right = self.deleteNode(root.right, min_node_greater.val)

        return root
        