class Node:
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

def findBST(root, val):
    if not root:
        return None
    
    if val > root.val:
        return findBST(root.right, val)
    elif val < root.val:
        return findBST(root.left, val)
    
    return root