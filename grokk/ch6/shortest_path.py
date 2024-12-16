# hashmap, hashtable, dict, adjacency list, associative array, etc.
from collections import deque

graph = {
    "A": ["B", "C"],
    "B": ["A", "D"],
    "C": ["A", "D"],
    "D": ["B", "C"]
}

def shortest_path(graph: dict, start, end):
    # if one item only in graph check
    if start == end:
        return [start]
    queue = deque([[start]]) # two brackets because iterable needs brackets, and this is a list of lists iterable
    # set is faster than list
    searched = set()
    while queue: # while queue has items
        path = queue.popleft()
        node = path[-1] # always want the last node in the path in queue, since the queue we
        # are iterating is a list of paths
        
        if node == end:
            return path

        if node not in searched:
            searched.add(node)
            for neighbor in graph.get(node, []):
                if neighbor not in searched:
                    new_path = path + [neighbor]
                    queue.append(new_path)


    return [] # returns empty, if start to end is simply not possible!

print(shortest_path(graph, "A", "C"))