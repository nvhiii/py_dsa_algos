# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        arr = []

        def dfs(root, arr):
            if not root:
                return
            
            dfs(root.left, arr)
            arr.append(root.val)
            dfs(root.right, arr)

        dfs(root, arr)
        return arr
        
    
