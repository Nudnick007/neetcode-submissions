class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        c = Counter(students)
        res = len(students)
        for n in sandwiches:
            if c[n] > 0:
                c[n] -=1
                res -=1
            else:
                break
        return res