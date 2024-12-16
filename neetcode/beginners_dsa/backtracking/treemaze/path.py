"""
Q: Determine if a path exists from the root of the tree
to a leaf node. It may not contain any
zeroes"""

def find_path(root, path):
    if not root or root.val == 0:
        return False
    path.append(root.val)
    if not root.left and not root.right:
        return True
    if find_path(root.left, path):
        return True
    if find_path(root.right, path):
        return True
    
    path.pop()
    return False