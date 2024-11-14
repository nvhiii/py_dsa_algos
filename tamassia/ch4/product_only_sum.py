def product_only_sum(m, n):
    if n == 0:
        return 0
    else:
        return m + product_only_sum(m, n - 1)
    
print(product_only_sum(6, 7))