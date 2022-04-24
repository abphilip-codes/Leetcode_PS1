# 566
# https://leetcode.com/problems/reshape-the-matrix/

class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        if m * n != r * c: return mat
        arr = [mat[row][col] for row in range(m) for col in range(n)]
        return [arr[i:i + c] for i in range(0, r * c, c)]