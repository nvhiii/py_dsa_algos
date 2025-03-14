def stepping(steps):

    def dfs(i):
        if i >= steps:
            return i == steps
        return dfs(i + 1) + dfs(i + 2)

    return dfs(0)