# 976
# https://leetcode.com/problems/largest-perimeter-triangle/

class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        for z in range(len(nums)-3,-1,-1):
            if(nums[z]+nums[z+1]>nums[z+2]): return sum(nums[z:z+3])
        return 0