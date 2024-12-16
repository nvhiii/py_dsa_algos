class Node:
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.right = right
        self.left = left

# tree set needs a set, no in built method for it this i think,
# maybe ordereddict?