# 1356
# https://leetcode.com/problems/sort-integers-by-the-number-of-1-bits/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        if(head.val==1 and not head.next): return int(1)
        else:
            ans, h = '', head
            while(h):
                ans += str(h.val)
                h = h.next
            s, l = 0, len(ans)
            for z in range(l-1,-1,-1):
                s += (2**z)*int(ans[l-1-z])
            return s