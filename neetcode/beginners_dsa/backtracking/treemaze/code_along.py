"""
Q: Determine if a path exists from the root of the tree
to a leaf node. It may not contain any zeroes."""

def p_root_leaf(root):
    if not root or root.val == 0:
        return False # root is invalid

    if not root.left and not root.right:
        return True
    if p_root_leaf(root.left):
        return True
    if p_root_leaf(root.right):
        return True
    
    return False