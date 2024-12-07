def adj_dfs(node, target, adj, visited):
    """Count paths"""
    if node in visited:
        return 0
    if node == target:
        return 1
    
    count = 0
    for neighbor in adj[node]:
        count += adj_dfs(neighbor, target, adj, visited)
        visited.add(neighbor) # add the node

    visited.remove(node)
    return count
    
