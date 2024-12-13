def comb_sum(nums, target):
    # return list of lists that sum into target
    res = []
    def dfs(i, arr, currSum):
        if currSum == target:
            res.append(arr.copy())
            return
        if i >= len(nums) or currSum > target:
            return
        
        arr.append(nums[i])
        dfs(i, arr, currSum + nums[i])
        arr.pop()
        dfs(i + 1, arr, currSum)

    dfs(0, [], 0)
    return res