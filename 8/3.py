# 389
# https://leetcode.com/problems/find-the-difference/

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        for z in s:
            if(z in t): t = t.replace(z,'',1)
        return t