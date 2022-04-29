# 1603
# https://leetcode.com/problems/design-parking-system/

class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        return sorted(arr, key = lambda x: (bin(x).count('1'), x))