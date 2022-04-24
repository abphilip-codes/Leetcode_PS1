# 566
# https://leetcode.com/problems/reshape-the-matrix/

class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        x, y = len(mat), len(mat[0])
        if(x*y!=r*c): return mat
        arr = [mat[a][b] for a in range(x) for b in range(y)]
        return [arr[k:k+c] for k in range(0, r*c, c)]