class TreeNode:
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

def insertNode(root, val):
    if not root:
        return TreeNode(val) # initialize root
    
    if val > root.val:
        root.right = insertNode(root.right, val)
    elif val < root.val:
        root.left = insertNode(root.left, val)

    return root # returns root for current recursive subtree