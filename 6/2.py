# 283
# https://leetcode.com/problems/move-zeroes/

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        s=0
        for z in range(len(nums)):
            if not nums[s]:
                nums.pop(s)
                nums.append(0)
            else: s+=1