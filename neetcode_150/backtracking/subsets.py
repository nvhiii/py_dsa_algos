class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        subset = []
        def dfs(i): # i is the index
            if i >= len(nums): # out of bounds
                result.append(subset.copy())
                return
            
            subset.append(nums[i])
            dfs(i + 1) # here, we run dfs on the tree that includes the num at ith index for the subset

            subset.pop() # removed the nums[i] from the subset, hence [] branch
            dfs(i + 1)

        dfs(0)
        return result