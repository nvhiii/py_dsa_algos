# bfs
from collections import deque
def bfs(root):
    queue = deque()
    if root:
        queue.append(root)

    while len(queue) > 0:
        for i in range(len(queue)):
            curr = queue.popleft()
            if curr.left:
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)