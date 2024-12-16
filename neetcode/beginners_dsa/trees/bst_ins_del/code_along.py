class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def insert_bst(root, val):
    if not root:
        return TreeNode(val) # creates tree of height 1 node
    
    if val > root.val:
        root.right = insert_bst(root.right, val)
    elif val < root.val:
        root.left = insert_bst(root.left, val)
    
    return root

def findMinNode(root):
    curr = root
    while curr and curr.left:
        curr = curr.left # left nodes always have less value
    return curr

def findMaxNode(root):
    curr = root
    while curr and curr.right:
        curr = curr.right
    return curr

def delete_node(root, val):
    if not root:
        return None
    
    if val > root.val:
        root.right = delete_node(root.right, val)
    elif val < root.val:
        root.left = delete_node(root.left, val)
    else: # got to target node w specified val
        if not root.left:
            return root.right
        elif not root.right:
            return root.left # cases for 1 or less children
        else:
            # in-order successor
            min_node_greater = findMinNode(root.right)
            root.val = min_node_greater.val # the target node val overwritten
            root.right = delete_node(root.right, min_node_greater.val)
    return root # should be the tree in sucessor order