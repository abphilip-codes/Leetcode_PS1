# 1822
# https://leetcode.com/problems/sign-of-the-product-of-an-array/

class Solution:
    def arraySign(self, nums: List[int]) -> int:
        n=0
        for z in nums:
            if(z==0): return 0
            if(z<0): n+=1
        return 1 if(n%2==0) else -1