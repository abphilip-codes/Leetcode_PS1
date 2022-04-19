# 1281
# https://leetcode.com/problems/average-salary-excluding-the-minimum-and-maximum-salary/

class Solution:
    def average(self, salary: List[int]) -> float:
        return sum(sorted(salary)[1:-1])/(len(salary)-2)