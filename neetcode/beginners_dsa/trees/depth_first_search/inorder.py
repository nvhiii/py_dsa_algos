def inorder(root):
    # left until null, print, then check right of parent node if exists
    if not root:
        return
    
    inorder(root.left)
    print(root.val)
    inorder(root.right)

tree = [1, 2, 3, 4, 5, 6, 7]