# 1572
# https://leetcode.com/problems/matrix-diagonal-sum/

class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        ans=0
        for z in range(len(arr)+1):
            for y in range(z):
                if(len(arr[y:z])%2!=0):
                    ans+=sum(arr[y:z])
        return ans