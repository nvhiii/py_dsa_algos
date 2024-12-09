"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
from collections import deque
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # we have list of nodes
        # indexing starts at 1, each list index within list of nodes represents the node itself, and the array contents are its neighbors
        # we want to clone this
        # can still have node with no edges at all -> basecase?, actually empty init node is basecase

        # need cloned hashmap, graph = adj list easily
        # base case - no node, none
        # queue, for bfs
        # initiliaze queue with node
        # initialize first val in hm using node class def
        # iterate the queue (which iterates each node)
        # pop item, get node
        # iterate its neighbors
        # check if not in hm
        # if not, append q + create new key for the neighbor
        # if it is is hm, then append to curr neighbors the ref to the cloned neighbor
        # return the cloned arr pointing to first node

        if not node:
            return None

        cloned = {}
        q = deque([node])
        cloned[node] = Node(node.val)

        while q:
            curr = q.popleft() # gives us the node itself
            for n in curr.neighbors:
                if n not in cloned: # not a key yet
                    cloned[n] = Node(n.val)
                    q.append(n) # append this neighbor node
                # already a key case
                cloned[curr].neighbors.append(cloned[n])

        return cloned[node]
