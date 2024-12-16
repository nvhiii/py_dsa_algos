def path_sum(root, target):
    # no store, return t / f
    if not root:
        return False
    
    if not root.left and not root.right:
        return root.val == target
    
    r = target - root.val
    return path_sum(root.left, r) or path_sum(root.right, r)
    