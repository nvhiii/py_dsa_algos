class Node:
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

def insertBST(root: "Node", val):
    if not root:
        return Node(val)
    
    if val < root.val:
        root.left = insertBST(root.left, val)
    elif val > root.val:
        root.right = insertBST(root.right, val)

    return root