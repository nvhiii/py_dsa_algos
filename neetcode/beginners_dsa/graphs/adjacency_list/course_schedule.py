class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # edge list, where in order to take a course a, need to take b [a,b]
        # check for cycles, that means no way to complete all
        # check if a prereq has no prereqs, then possible
        # use dfs
        # from edges, create a adjlist
        # have a hashset to track currently visiting or nah (if course is already visited, then cycle detected)
        # base case: alr exists in visiting, or hashmap[course] == [], meaning we def can complete all course then
        # then we append the course to the hashset
        # then iterate the prereqs of the curr course, check recursively if possible on it
        # return false if not
        # then back track
        # then return True

        # we apply the dfs algo to a loop

        coursepreq = { i : [] for i in range(numCourses)} # this ensures each course has its own "index" in hashmap
        # populate hashmap
        for crs, pre in prerequisites:
            coursepreq[crs].append(pre)

        visiting = set()

        def dfs(course):
            if course in visiting:
                return False
            if coursepreq[course] == []:
                return True

            visiting.add(course)
            for preq in coursepreq[course]: # iter neighbors of curr course
                if not dfs(preq):
                    return False
            # backtrack
            visiting.remove(course)
            coursepreq[course] = []
            return True

        # now apply dfs to all elements in adj list
        for c in range(numCourses):
            if not dfs(c):
                return False
        return True