def findPath(root):
    if not root or root.val == 0:
        return False
    
    if not root.left and not root.right:
        return True
    if findPath(root.left):
        return True
    elif findPath(root.right):
        return True
    
    return False