# need 3 dicts, 1 graph, 1 cost, 1 relationship {parent: child}
# 4 steps
# find lowest cost node
# check path to each neighbor, update w/ cheapest
# loop 1st and 2nd step
# return path

graph = {
    "start": {"a": 6, "b": 2},
    "a": {"fin": 1},
    "b": {"a": 3, "fin": 5},
    "fin": {}
}

infinity = float("inf")
costs = {"a": 6, "b": 2, "fin": infinity}
parents = {"a": "start", "b": "start", "fin": None}

def nahis_dijkstra(graph, costs, parents, end):
    visited = set() # o1
    # helper for step 1
    def find_cheapest_node(costs):
        lowest = float("inf")
        cheapest_node = None
        for node in costs:
            cost = costs[node]
            # now do comparison
            if cost < lowest and node not in visited:
                lowest = cost
                cheapest_node = node
        return cheapest_node
    
    # find lowest cost node
    # step 1, find curr cheapest
    node = find_cheapest_node(costs) # must be costs, not graph bc that returns dicts
    while node is not None:
        # get cost of node for addition
        cost = costs[node]
        # get neighbors
        neighbors = graph[node] # returns a dict eg: {A: 6, B: 2}
        for neighbor in neighbors.keys():
            # calc cost from parent to child
            new_cost = cost + neighbors[neighbor]
            # step 2 compare current costs of neighbors
            if costs[neighbor] > new_cost: # compare if new path cost is cheaper than current cost to neighbor node, # checking neighbors cost and updating if necessary
                costs[neighbor] = new_cost # update costs hashmap
                parents[neighbor] = node # update parents hashmap

        # update checked nodes
        visited.add(node)
        # recursive call to cheapest node
        # step 3 loop
        node = find_cheapest_node(costs)

        # now reconstruct path
        # step 4
        path = []
        # start at current
        node_to_trace = end # this is last node
        # eg
        # node2: node3
        # node3: end
        while node_to_trace:
            path.append(node_to_trace)
            node_to_trace = parents.get(node_to_trace)
        path = path[::-1]

    return path, costs[end]

path, cost = nahis_dijkstra(graph, costs, parents, "fin")
print("Path:", path)
print("Cost:", cost)
        


