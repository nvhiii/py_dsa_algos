class Node:
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

def findSmallestNode(root):
    curr = root
    while curr and curr.left:
        curr = curr.left
    return curr

def deleteNode(root: "Node", val):
    if not root:
        return None

    if val < root.val:
        root.left = deleteNode(root.left, val)
    elif val > root.val:
        root.right = deleteNode(root.right, val)
    else:
        # we got to right pos
        if not root.left:
            return root.right
        elif not root.right:
            return root.left
        else:
            # in order successor
            mvg = findSmallestNode(root.right)
            root.val = mvg.val
            root.right = deleteNode(root.right, mvg.val)

    return root