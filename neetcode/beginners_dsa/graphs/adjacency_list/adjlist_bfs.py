from collections import deque

def adjlist_bfs(node, target, adjlist, visited):
    q = deque([node])
    visited.add(node)
    length = 0
    while q:
        for _ in range(len(q)):
            node = q.popleft()
            # base case
            if node == target:
                return length
            
            for neighbor in adjlist[node]:
                # base case
                if neighbor not in visited:
                    q.append(neighbor)
                    visited.add(neighbor)

        length += 1

    return -1