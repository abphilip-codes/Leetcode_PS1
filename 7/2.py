# 566
# https://leetcode.com/problems/reshape-the-matrix/

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        d, s = {}, []
        for z in nums2:
            while s and z>s[-1]:
                d[s.pop()] = z
            s.append(z)  
        for i, z in enumerate(nums1):
            nums1[i] = d.get(z,-1)
        return nums1