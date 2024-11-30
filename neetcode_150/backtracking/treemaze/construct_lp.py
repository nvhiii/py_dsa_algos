def construct_leaf_path(root, arr):
    if not root or root.val == 0:
        return False
    
    arr.append(root.val)
    if not root.left and not root.right:
        return True
    if construct_leaf_path(root.left, arr):
        return True
    if construct_leaf_path(root.right, arr):
        return True
    
    arr.pop()
    return False