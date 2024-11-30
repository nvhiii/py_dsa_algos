class Node:
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

def findBST(root, val):
    if not root:
        return None
    
    if val < root.val:
        root.left = findBST(root.left, val)
    elif val > root.val:
        root.right = findBST(root.right, val)
    else:
        return root