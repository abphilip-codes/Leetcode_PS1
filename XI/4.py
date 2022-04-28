# 217
# https://leetcode.com/problems/contains-duplicate/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        def f(k,ans,p):
            if(not k): return 0
            if(not k.left and not k.right and p==1):
                ans+=k.val
                return ans
            return(f(k.left,ans,1) + f(k.right,ans,0))
        return f(root,0,0)