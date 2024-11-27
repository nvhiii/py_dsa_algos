def rorder(root):
    # first right, then val, then check left of parent node
    if not root:
        return
    rorder(root.right)
    print(root.val)
    rorder(root.left)