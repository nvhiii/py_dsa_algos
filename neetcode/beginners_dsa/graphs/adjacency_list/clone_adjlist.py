"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
from collections import deque
from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # notes
        # node class given
        # goal: deep copy of a graph (hash map)
        # val = node index
        
        # approach
        # bfs or dfs, ill go with bfs
        # base case / edge: if not node
        # have a queue for each node
        # have cloned hm
        # populate hm + queue with first node
        # iterate the q, then iterate each ndoe neighbors + appropriately populate
        # return cloned hm and ref to original node
        # space + time = o(v + e), v = vertice, e = edge

        if not node:
            return None

        q = deque([node])
        cloned = {}
        cloned[node] = Node(node.val) # from node class

        while q:
            curr = q.popleft()
            for n in curr.neighbors: # from node class
                if n not in cloned: # case for if neighbor not a key val yet in cloned hm
                    q.append(n)
                    cloned[n] = Node(n.val)
                # case for the n is a key val already
                cloned[curr].neighbors.append(cloned[n])

        return cloned[node]
    