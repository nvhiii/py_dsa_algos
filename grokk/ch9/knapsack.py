def knapsack(weights, values, W):
    n = len(weights)
    # Create a (n+1) x (W+1) matrix initialized with 0
    dp = [[0] * (W + 1) for _ in range(n + 1)]

    # Populate the matrix
    for i in range(1, n + 1):
        for w in range(W + 1):
            if weights[i-1] <= w:
                # Either take the item or leave it
                dp[i][w] = max(dp[i-1][w], dp[i-1][w - weights[i-1]] + values[i-1])
            else:
                dp[i][w] = dp[i-1][w]

    return dp[n][W]

# Example usage:
weights = [2, 3, 4, 5]
values = [3, 4, 5, 6]
W = 5
print("Maximum value:", knapsack(weights, values, W))  # Output: Maximum value: 7
