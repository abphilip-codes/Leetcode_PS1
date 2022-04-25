# 389
# https://leetcode.com/problems/find-the-difference/

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s1 = sorted(list(s))
        t1 = sorted(list(t))
        for z in range(len(s1)):
            if(s1[z]!=t1[z]): return t1[z]
        else: return t1[-1]