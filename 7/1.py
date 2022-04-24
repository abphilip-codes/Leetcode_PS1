# 1572
# https://leetcode.com/problems/matrix-diagonal-sum/

class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        ans, n = 0, len(mat)
        for z in range(n): ans+=(mat[z][z]+mat[z][-1-z])
        if(n%2): ans-=(mat[n//2][n//2])
        return ans