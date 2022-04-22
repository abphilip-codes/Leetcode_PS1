# 1502
# https://leetcode.com/problems/can-make-arithmetic-progression-from-sequence/

class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort()
        k = arr[1]-arr[0]
        for z in range(2, len(arr)):
            if(arr[z]-arr[z-1]!=k): return False
        return True