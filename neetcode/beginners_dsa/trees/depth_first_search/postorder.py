def postorder(root):
    # first left, right then print then parent
    if not root:
        return
    postorder(root.left)
    postorder(root.right)
    print(root.val)