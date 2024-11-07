def top_k_freq(nums: list, k: int) -> list:
    count = {}
    freq = [[] for i in range(len(nums) + 1)] # buckets for each freq, holds numbers w that freq

    for num in nums:
        count[num] = 1 + count.get(num, 0)
    for num, count in count.items():
        freq[count].append(num) # freq holds nums for each count

    items = []
    for i in range(len(freq) - 1, 0, -1): # ends at 0, but is exclusive hence ends at 1
        for num in freq[i]:
            items.append(num)
            if len(items) == k:
                return items
            
nums = [1, 2, 3, 4, 4, 4, 3, 3, 3, 2, 5, 5, 5]
print(top_k_freq(nums, 3))