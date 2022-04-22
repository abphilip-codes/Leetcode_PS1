# 589
# https://leetcode.com/problems/n-ary-tree-preorder-traversal/

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

def k(child, l):
    if not child: return
    l.append(child.val)
    for child in child.children:
        k(child, l)

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        ans = []
        if not root: return ans
        k(root, ans)
        return ans