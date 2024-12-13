def preorder(root):
    # first root node print, then left then check right then recur
    if not root:
        return
    print(root.val)
    preorder(root.left)
    preorder(root.right)
    