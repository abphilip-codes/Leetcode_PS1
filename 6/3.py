# 1232
# https://leetcode.com/problems/check-if-it-is-a-straight-line/

class Solution:
    def checkStraightLine(self, c: List[List[int]]) -> bool:
        dx, dy = c[0][0]-c[1][0], c[0][1]-c[1][1]
        for z in range(1,len(c)-1):
            if((c[z][0]-c[z+1][0])*dy !=  
            (c[z][1]-c[z+1][1])*dx): return False
        return True