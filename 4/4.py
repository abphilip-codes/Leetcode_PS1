# 1779
# https://leetcode.com/problems/find-nearest-point-that-has-the-same-x-or-y-coordinate/

class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        m, ans = math.inf, -1
        for z in range(len(points)):
            if(points[z][0]!=x and points[z][1]!=y): continue
            d = abs(points[z][0]-x)+abs(points[z][1]-y)
            if(m>d): m, ans = d, z
        return ans