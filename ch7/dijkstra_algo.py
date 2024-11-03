# dijkstra algo cannot use negative weights (use bellman ford)
# cannot be used on graphs that have cycles as well

# graph is the hashmap containing all hash maps

def dijkstra(graph, costs, parents, start, end):
    # Keep track of processed nodes
    processed = []  

    # helper
    def find_lowest_cost_node(costs):
        lowest_cost = float("inf")
        lowest_cost_node = None
        for node in costs:
            cost = costs[node]
            if cost < lowest_cost and node not in processed:
                lowest_cost = cost
                lowest_cost_node = node
        return lowest_cost_node

    # first find lowest cost node to go to based on first node
    # Start the algorithm from the starting node
    node = find_lowest_cost_node(costs)
    while node is not None:
        cost = costs[node] # assigns price to node in costs hashmap
        neighbors = graph[node] # assigns neighbors to node in graph hashmap, returns a dict
        for n in neighbors.keys():
            new_cost = cost + neighbors[n] # updates cost of the curr path in neighbors hashmap
            if costs[n] > new_cost:
                costs[n] = new_cost
                parents[n] = node
        processed.append(node)
        node = find_lowest_cost_node(costs)

    # Build the path from start to end
    # this is reverse iterating the graph hashmap
    path = []
    current = end # start from end of path, "fin"
    while current:
        path.append(current)
        current = parents.get(current) # iterate through parents graph
    path = path[::-1]  # Reverse to get path from start to end

    return path, costs[end]  # Return the path and the total cost to reach the end

# Define the graph, costs, and parents
# this is a weighted graph, identified via two nested dicts
# graph contains nodes as keys, dicts and values
# inner dict has the neighbors for the outer key, and its corresponding edge weight 
graph = {
    "start": {"a": 6, "b": 2},
    "a": {"fin": 1},
    "b": {"a": 3, "fin": 5},
    "fin": {}
}

infinity = float("inf")
costs = {"a": 6, "b": 2, "fin": infinity}
parents = {"a": "start", "b": "start", "fin": None}

# Call the dijkstra function
path, cost = dijkstra(graph, costs, parents, "start", "fin")
print("Path:", path)
print("Cost:", cost)
