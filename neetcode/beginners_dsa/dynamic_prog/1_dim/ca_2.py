# top down fib
def top_down_fib(n):
    if n < 2:
        return n
    
    dp = [0, 1]
    i = 0
    while i <= n:
        temp = dp[1] # store this to change 0th index
        dp[1] = dp[0] + dp[1]
        dp[0] = temp
        i += 1
    return dp[1]