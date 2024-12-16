# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # preorder is the val we iter to, shows the order
        # inorder tells us which sides to add, left sub or right (iter all elements until # bound set)
        pi = ii = 0
        def dfs(bound):
            nonlocal pi,ii
            if pi >= len(preorder):
                return None
            elif inorder[ii] == bound: # we reach the limit of preorder
                ii += 1 # skip that node
                return None
            
            # root
            root = TreeNode(preorder[pi])
            pi += 1

            # recur
            root.left = dfs(root.val) # val must be changed for less than
            root.right = dfs(bound)

            return root

        return dfs("inf")

