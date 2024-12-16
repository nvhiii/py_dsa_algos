class TreeNode:
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

def findMinNode(root):
    curr = root
    while curr and curr.left: # bst always sorted
        curr = curr.left
    return curr

def deleteNode(root, val):
    if not root:
        return None # we cant remove something from nothing
    
    # now get to target node w val
    if val > root.val:
        root.right = deleteNode(root.right, val)
    elif val < root.val:
        root.left = deleteNode(root.left, val)
    else:
        # we got to target val node
        # handle cases for root w less than or equal to 1 child
        if not root.left:
            return root.right
        elif not root.right:
            return root.left
        else:
            # in order successor order
            minValGreater = findMinNode(root.right)
            root.val = minValGreater.val
            root.right = deleteNode(root.right, minValGreater.val)

    return root