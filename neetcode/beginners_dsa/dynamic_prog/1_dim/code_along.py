# optimized fib, we dont calculate smaller fibs as we go on in this recursion
# this makes time go from 2^n, where n is the height, and 2 factor per lvl
# the new time is now o(n), linear 
def memoized_fib(n, cache): # nth fib number
    if n <= 1:
        return n
    if n in cache:
        return cache[n] # memoization
    
    # add to hashmap
    cache[n] = memoized_fib(n - 1, cache) + memoized_fib(n - 2, cache) # prev two nums
    return cache[n]