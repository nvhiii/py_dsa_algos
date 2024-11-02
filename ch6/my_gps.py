from collections import deque

# Adjacency list for locations
locations = {
    "Home": ["Library", "Cafe"],
    "Library": ["Home", "Cafe", "Park"],
    "Cafe": ["Home", "Library", "Mall"],
    "Park": ["Library", "Mall"],
    "Mall": ["Cafe", "Park", "Gym"],
    "Gym": ["Mall"]
}

def my_gps(graph: dict, start: str, end: str):
    # do check if location to start and end is same node
    if start == end:
        return [start]
    queue = deque([[start]]) # list of paths, find shortest
    searched_nodes = set() # O1
    while queue: # while not empty
        path = queue.popleft()
        location = path[-1]

        if location == end:
            return path_str(path) # formats the list

        if location not in searched_nodes:
            searched_nodes.add(location)
            for neighbor in graph.get(location, []):
                new_path = path + [neighbor]
                queue.append(new_path)

    return "No possible (legal) path found"

def path_str(path):
    if not path:
        return "No path found"
    
    if len(path) == 1:
        return f"The path is simply the location: {path[0]}"
    
    # Build the formatted string for paths with length 2 or more
    directions = [f"Start at {path[0]}"]
    for i in range(1, len(path) - 1):
        directions.append(f"Next, go to {path[i]}")
    directions.append(f"End at {path[-1]}")

    return ". ".join(directions) + "."


print(my_gps(locations, "Home", "Gym"))
