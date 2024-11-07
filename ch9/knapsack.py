items_to_steal = [("guitar", 1500, 1), ("stereo", 3000, 4), ("laptop", 2000, 3)]
# item, price, weight
def knapsack(items: list, sack_limit: int):
    # dynamic prog split into matrix m by n rows col
    
    # first create matrix len(items) x range(sack_limit)
    max_prices = [[0 for _ in range(len(sack_limit+1))] for _ in range(len(items+1))] # range is exclusive

    # populate
    pass