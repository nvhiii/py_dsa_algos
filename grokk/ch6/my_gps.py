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
        return path_str([start])
    queue = deque([[start]]) # list of paths, find shortest
    searched_nodes = set() # O1
    while queue: # while not empty
        path = queue.popleft() # returns a list of nodes, locations
        location = path[-1] # returns last item/location of list, aka path

        if location == end: # if last item in this path is specified end, this returns
            return path_str(path) # formats the list

        if location not in searched_nodes: # can be searched locatiuons to be more concise
            searched_nodes.add(location)
            for neighbors in graph.get(location, []): # renamed to neighbors, since this returns list
                new_path = path + [neighbors] # create new path using previous list and current list
                queue.append(new_path) # add to queue, rinse and repeat

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

# my bfs takeaway:
# We check if we have checked the last item in each path, last item of the list. Then we  get a list where the key is the last item of the previous list in the queue. then we create a new item using this given list and the previous list and we append this to the queue, all up until the last item in the list popped from the queue is the ending.

# Starting with an initial path.
# Expanding the path by adding neighbors of the last node in each path.
# Storing and exploring these expanded paths one-by-one.
# Stopping when we find the destination, thus guaranteeing the shortest path.