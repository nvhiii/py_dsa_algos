class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        pref = Counter(students) # their preferences list
        res = len(students)

        for s in sandwiches:
            if pref[s] > 0:
                pref[s] -= 1
                res -= 1
            else:
                return res

        return res # in the case all sandwiches are eaten