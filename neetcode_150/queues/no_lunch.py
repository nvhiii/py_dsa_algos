def countStudents(self, students, sandwiches):
        """
        :type students: List[int]
        :type sandwiches: List[int]
        :rtype: int
        """
        result = len(students) # returned value to see which students cannot eat
        c = Counter(students)

        for s in sandwiches: # we iterate the sandwiches, bc order does matter here
            if c[s] > 0:
                result -= 1 # num of students decrease bc at least 1 student can eat this sandwich
                c[s] -= 1 # decrease the counter for the specified student
            else:
                return result # meaning not a single student can eat the sandwwich
        return result