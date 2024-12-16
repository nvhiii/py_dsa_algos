# edges = [["A", "B"], ["B", "C"], ["B", "E"], ["C", "E"], ["E", "D"]]

# # create adj list

# adj_list = {}

# for curr, dst in edges:
#     # these are the cases if the nodes dont exist as keys
#     if curr not in adj_list:
#         adj_list[curr] = set()
#     if dst not in adj_list:
#         adj_list[dst] = set()

#     # if they do exist already
#     adj_list[curr].append(dst)

# now lets try it with a graphnode class implementation

class GraphNode:
    def __init__(self, val):
        self.val = val
        self.neighbors = [] # list of its neighbors, can also be a set

a = GraphNode(5)
b = GraphNode(6)
a.neighbors.append(b)

nodes = [a, b]
# now recreate this in a hashmap
adj_list = {}

for curr in nodes:
    # in this first step, we initialize the key (neighbors not populated yet)
    if curr not in adj_list:
        adj_list[curr] = []
    # second step, we add values to list of the key value
    for neighbor in curr.neighbors:
        adj_list[curr].append(neighbor)
