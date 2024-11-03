# dijkstra algo cannot use negative weights (use bellman ford)
# cannot be used on graphs that have cycles as well

def dijkstra(graph, costs, parents, start, end):
    # Keep track of processed nodes
    processed = []

    def find_lowest_cost_node(costs):
        lowest_cost = float("inf")
        lowest_cost_node = None
        for node in costs:
            cost = costs[node]
            if cost < lowest_cost and node not in processed:
                lowest_cost = cost
                lowest_cost_node = node
        return lowest_cost_node

    # Start the algorithm from the starting node
    node = find_lowest_cost_node(costs)
    while node is not None:
        cost = costs[node]
        neighbors = graph[node]
        for n in neighbors.keys():
            new_cost = cost + neighbors[n]
            if costs[n] > new_cost:
                costs[n] = new_cost
                parents[n] = node
        processed.append(node)
        node = find_lowest_cost_node(costs)

    # Build the path from start to end
    path = []
    current = end
    while current:
        path.append(current)
        current = parents.get(current)
    path = path[::-1]  # Reverse to get path from start to end

    return path, costs[end]  # Return the path and the total cost to reach the end

# Define the graph, costs, and parents
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
