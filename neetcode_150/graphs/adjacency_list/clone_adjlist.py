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
        # cloned adjlist, hashmap aka dict
        # bfs

        # NEED THIS
        if not node:
            return None

        cloned = {} # HM
        q = deque([node])
        cloned[node] = Node(node.val)

        while q:
            curr = q.popleft() # node
            for n in curr.neighbors:
                if n not in cloned: # if it doesnt have set of neighbors in new adj list
                    q.append(n)
                    cloned[n] = Node(n.val)
                # if it already exists as a key
                cloned[curr].neighbors.append(cloned[n])

        return cloned[node]