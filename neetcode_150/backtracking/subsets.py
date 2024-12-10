class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # power set of a list of nums
        # empty list returns empty list
        # hard part is keeping track of same subsets, basically reordered

        # [1] = [[], [1]]

        # brute force:
        # go through each item in the list, then branch out n times for the n number of items in list, this solution doesnt account for uniques tho
        # one way is to back track optimize, so include branch to include curr node val or not.
        # dfs?
        # base case: if i >= len(nums), nothing to iterate, so we append copy of subset then return
        # then append, then do dfs w paths of branch

        result = []
        subset = []
        def dfs(i):
            if i >= len(nums):
                result.append(subset.copy())
                return

            subset.append(nums[i])
            dfs(i + 1) # curr valid path

            subset.pop()
            dfs(i + 1) # skipped

        dfs(0)
        return result