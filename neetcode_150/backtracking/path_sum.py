def path_sum(root, target):
    if not root:
        return None
    
    if not root.left and not root.right:
        return root.val == target
    
    remaining = target - root.val
    return path_sum(root.left, remaining) or path_sum(root.right, remaining)