# 242
# https://leetcode.com/problems/valid-anagram/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if(root): 
            return max(self.maxDepth(root.left)+1, self.maxDepth(root.right)+1)
        return 0