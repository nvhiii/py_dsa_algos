from collections import deque

heart = {
    "nahi" : ["money", "family", "time", "cars", "gym"],
    "money": ["time"],
    "family": ["nahi", "cars"],
    "time": ["nahi"],
    "cars": ["money"],
    "gym": ["money"]
}

def ptheart(graph: dict, start, end):
    if start == end:
        return [start]
    # create queue
    queue = deque([[start]])
    visited = set()
    while queue:
        path = queue.popleft() # returns list
        last_location = path[-1]
        if last_location == end:
           return path # if path has end location as last, return
        if last_location not in visited:
            visited.add(last_location)
            for neighbors in graph.get(last_location, []):
                new_path = path + [neighbors]
                queue.append(new_path)

    return []

print(ptheart(heart, "nahi", "money"))